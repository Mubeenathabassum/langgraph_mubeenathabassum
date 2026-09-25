import os
import io
import sys
import traceback
from typing import TypedDict, List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes

# -----------------------------
# Gemini API Key (Render)
# -----------------------------
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

# -----------------------------
# LangGraph State
# -----------------------------
class CrewState(TypedDict):
    messages: List[BaseMessage]
    code: Optional[str]
    report: Optional[str]

# -----------------------------
# Tools
# -----------------------------
@tool
def run_python_code(code: str) -> str:
    """Execute Python code and return output."""

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
    """Generate test cases using Gemini."""

    prompt = f"""
    You are a Senior QA Engineer.

    Generate 3 to 5 numbered test cases for this coding task:

    {task_description}

    Include normal and edge cases.
    """

    return llm.invoke(prompt).content


# -----------------------------
# LangGraph Nodes
# -----------------------------
def developer_node(state: CrewState):
    task = state["messages"][-1].content

    prompt = f"""
    Write clean Python code for the following task.

    Task:
    {task}

    Return ONLY Python code.
    """

    code = llm.invoke(prompt).content
    code = code.replace("```python", "").replace("```", "").strip()

    return {"code": code}


def tester_node(state: CrewState):
    task = state["messages"][-1].content

    tests = generate_test_cases.invoke(task)
    output = run_python_code.invoke({"code": state["code"]})

    report = f"""
Execution Output
----------------
{output}

Generated Test Cases
--------------------
{tests}
"""

    return {"report": report}


# -----------------------------
# Build LangGraph Workflow
# -----------------------------
workflow = StateGraph(CrewState)

workflow.add_node("developer", developer_node)
workflow.add_node("tester", tester_node)

workflow.add_edge(START, "developer")
workflow.add_edge("developer", "tester")
workflow.add_edge("tester", END)

graph = workflow.compile()

# -----------------------------
# FastAPI + LangServe
# -----------------------------
app = FastAPI(
    title="LangGraph Coding Agent",
    version="1.0"
)

class TaskRequest(BaseModel):
    task: str

@app.get("/")
def home():
    return {"status": "LangGraph Running"}

@app.post("/generate")
def generate(request: TaskRequest):
    result = graph.invoke({
        "messages": [HumanMessage(content=request.task)]
    })

    return result

# Student Tribe Playground Route
add_routes(app, graph, path="/agent")
