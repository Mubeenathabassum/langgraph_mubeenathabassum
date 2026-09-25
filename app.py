import os
import io
import sys
import traceback
from typing import TypedDict, List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.tools import tool
from langchain_core.runnables import RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langserve import add_routes

# --------------------------------------------------
# Gemini LLM
# --------------------------------------------------
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

# --------------------------------------------------
# Graph State
# --------------------------------------------------
class CrewState(TypedDict):
    messages: List[BaseMessage]
    code: Optional[str]
    report: Optional[str]

# --------------------------------------------------
# Tools
# --------------------------------------------------
@tool
def run_python_code(code: str) -> str:
    """Execute Python code and return output or error."""

    clean_code = code.replace("```python", "").replace("```", "").strip()

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
        exec(clean_code, {"__builtins__": __builtins__}, {})
        output = new_stdout.getvalue()
    except Exception:
        output = traceback.format_exc()
    finally:
        sys.stdout = old_stdout

    return output if output else "Success (No Output)"


@tool
def generate_test_cases(task_description: str) -> str:
    """Generate test cases for a coding problem."""

    prompt = f"""
You are a Senior QA Engineer.

Generate 3-5 numbered test cases for this coding task.

Task:
{task_description}

Include edge cases also.
"""

    return llm.invoke(prompt).content


# --------------------------------------------------
# Developer Agent
# --------------------------------------------------
def developer_node(state: CrewState):

    task = state["messages"][-1].content

    prompt = f"""
Write clean Python code for this task.

Task:
{task}

Return ONLY Python code.
"""

    code = llm.invoke(prompt).content
    code = code.replace("```python", "").replace("```", "").strip()

    return {"code": code}


# --------------------------------------------------
# Tester Agent
# --------------------------------------------------
def tester_node(state: CrewState):

    task = state["messages"][-1].content

    tests = generate_test_cases.invoke(task)
    output = run_python_code.invoke({"code": state["code"]})

    report = f"""
EXECUTION OUTPUT

{output}

GENERATED TEST CASES

{tests}
"""

    return {"report": report}


# --------------------------------------------------
# LangGraph Workflow
# --------------------------------------------------
workflow = StateGraph(CrewState)

workflow.add_node("developer", developer_node)
workflow.add_node("tester", tester_node)

workflow.add_edge(START, "developer")
workflow.add_edge("developer", "tester")
workflow.add_edge("tester", END)

graph = workflow.compile()

# --------------------------------------------------
# FastAPI
# --------------------------------------------------
app = FastAPI(
    title="LangGraph Coding Assistant",
    version="1.0"
)


@app.get("/")
def health():
    return {"status": "LangGraph Agent Running"}


# --------------------------------------------------
# Playground Schema
# --------------------------------------------------
class TaskInput(BaseModel):
    task: str


class TaskOutput(BaseModel):
    generated_code: str
    execution_report: str


# --------------------------------------------------
# Playground Runnable
# --------------------------------------------------
def agent_runner(data: dict):

    task = data["task"]

    result = graph.invoke(
        {"messages": [HumanMessage(content=task)]}
    )

    return {
        "generated_code": result["code"],
        "execution_report": result["report"]
    }


playground_agent = RunnableLambda(agent_runner).with_types(
    input_type=TaskInput,
    output_type=TaskOutput
)

# Student Tribe Playground Route
add_routes(app, playground_agent, path="/agent")
