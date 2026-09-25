import os
import sys
import subprocess
import tempfile
from typing import TypedDict, List, Optional, Literal

from fastapi import FastAPI
from pydantic import BaseModel
from langserve import add_routes

from langchain_core.messages import HumanMessage, BaseMessage
from langchain_core.runnables import RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI

from langgraph.graph import StateGraph, START, END


# ============================================================
# GEMINI API
# ============================================================

GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set.")


model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=GOOGLE_API_KEY,
    temperature=0
)


# ============================================================
# STATE
# ============================================================

class CrewState(TypedDict):
    messages: List[BaseMessage]
    next_step: Optional[str]
    code: Optional[str]
    execution_output: Optional[str]
    report: Optional[str]
    manager_choice: Optional[str]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def response_to_text(response) -> str:
    content = response.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts = []

        for item in content:
            if isinstance(item, str):
                parts.append(item)

            elif isinstance(item, dict):
                if "text" in item:
                    parts.append(str(item["text"]))

        return "\n".join(parts)

    return str(content)


def clean_code(code: str) -> str:
    code = code.strip()

    if code.startswith("```"):
        lines = code.splitlines()

        if lines and lines[0].startswith("```"):
            lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        code = "\n".join(lines)

    return code.strip()


def run_python_code(code: str) -> str:
    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as f:
            f.write(code)
            temp_path = f.name

        result = subprocess.run(
            [sys.executable, temp_path],
            capture_output=True,
            text=True,
            timeout=10
        )

        output = result.stdout.strip()

        if result.stderr.strip():
            output += "\n" + result.stderr.strip()

        if not output:
            output = "Program executed successfully with no output."

        return output

    except subprocess.TimeoutExpired:
        return "Execution Error: Program exceeded the 10-second timeout."

    except Exception as e:
        return f"Execution Error: {str(e)}"

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)


# ============================================================
# LANGGRAPH NODES
# ============================================================

def task_input_node(state: CrewState):
    return {
        "messages": state["messages"],
        "next_step": "developer"
    }


def developer_node(state: CrewState):

    task = state["messages"][-1].content

    prompt = f"""
You are a Python developer.

User task:
{task}

Write a correct and executable Python program for the task.

IMPORTANT:
- Return ONLY Python code.
- Do not use Markdown.
- Do not use ``` fences.
- Do not explain the code.
"""

    response = model.invoke(
        [HumanMessage(content=prompt)]
    )

    code = clean_code(
        response_to_text(response)
    )

    return {
        "code": code,
        "next_step": "tester"
    }


def tester_node(state: CrewState):

    code = state["code"]

    # Execute generated Python code
    execution_output = run_python_code(code)

    prompt = f"""
You are a Senior QA Engineer.

Generated Python program:

{code}

Actual execution result:

{execution_output}

Create a SHORT and CLEAR testing report.

Use exactly this format:

Testing Status: PASSED or FAILED

Test Cases:
1. ...
2. ...
3. ...

Execution Check:
...

Summary:
...

Do not include:
- Date
- Tester name
- Long explanations
- Markdown tables
"""

    response = model.invoke(
        [HumanMessage(content=prompt)]
    )

    report = response_to_text(response).strip()

    return {
        "execution_output": execution_output,
        "report": report,
        "next_step": "manager"
    }


def manager_decision_node(state: CrewState):

    choice = state.get(
        "manager_choice",
        "store"
    )

    if choice == "store":
        return {
            "next_step": "archiver"
        }

    return {
        "next_step": "task_input"
    }


def archiver_node(state: CrewState):

    return {
        "next_step": "exit"
    }


# ============================================================
# BUILD LANGGRAPH
# ============================================================

graph = StateGraph(CrewState)

graph.add_node(
    "task_input",
    task_input_node
)

graph.add_node(
    "developer",
    developer_node
)

graph.add_node(
    "tester",
    tester_node
)

graph.add_node(
    "manager",
    manager_decision_node
)

graph.add_node(
    "archiver",
    archiver_node
)


graph.add_edge(
    START,
    "task_input"
)

graph.add_edge(
    "task_input",
    "developer"
)

graph.add_edge(
    "developer",
    "tester"
)

graph.add_edge(
    "tester",
    "manager"
)


def manager_route(state: CrewState):

    if state.get("manager_choice") == "store":
        return "archiver"

    return "task_input"


graph.add_conditional_edges(
    "manager",
    manager_route,
    {
        "archiver": "archiver",
        "task_input": "task_input"
    }
)

graph.add_edge(
    "archiver",
    END
)


rt_app = graph.compile()


# ============================================================
# INPUT / OUTPUT MODELS
# ============================================================

class AgentInput(BaseModel):
    input: str
    manager_choice: Literal[
        "store",
        "another"
    ] = "store"


class AgentOutput(BaseModel):
    status: str
    generated_code: Optional[str] = None
    execution_output: Optional[str] = None
    testing_report: Optional[str] = None
    error: Optional[str] = None


# ============================================================
# RUN AGENT
# ============================================================

def run_agent(data):

    try:

        # LangServe sends the input as a dictionary
        user_input = data["input"]

        manager_choice = data.get(
            "manager_choice",
            "store"
        )

        initial_state: CrewState = {
            "messages": [
                HumanMessage(
                    content=user_input
                )
            ],
            "next_step": None,
            "code": None,
            "execution_output": None,
            "report": None,
            "manager_choice": manager_choice
        }

        result = rt_app.invoke(
            initial_state,
            config={
                "recursion_limit": 20
            }
        )

        return {
            "status": "success",
            "generated_code": result.get("code"),
            "execution_output": result.get(
                "execution_output"
            ),
            "testing_report": result.get(
                "report"
            )
        }

    except Exception as e:

        return {
            "status": "error",
            "error": str(e)
        }


# ============================================================
# LANGSERVE
# ============================================================

agent_chain = RunnableLambda(
    run_agent
).with_types(
    input_type=AgentInput,
    output_type=AgentOutput
)


# ============================================================
# FASTAPI
# ============================================================

app = FastAPI(
    title="LangGraph Real-Time Developer Workflow",
    version="1.0"
)


add_routes(
    app,
    agent_chain,
    path="/agent"
)


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    import uvicorn

    port = int(
        os.environ.get(
            "PORT",
            8000
        )
    )

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port
    )
