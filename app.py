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
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes

# =====================================================
# GEMINI LLM
# =====================================================
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

# =====================================================
# STATE
# =====================================================
class CrewState(TypedDict):
    messages: List[BaseMessage]
    code: Optional[str]
    report: Optional[str]

# =====================================================
# TOOLS
# =====================================================
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
    """Generate 3–5 test cases using Gemini."""

    prompt = f"""
You are a Senior QA Engineer.

Generate 3 to 5 numbered test cases for the following coding task:

{task_description}

Include normal cases and edge cases.
"""

    return llm.invoke(prompt).content

# =====================================================
# LANGGRAPH NODES
# =====================================================
def developer_node(state: CrewState):
    task = state["messages"][-1].content

    prompt = f"""
Write a clean Python program for the following task.

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
### EXECUTION OUTPUT

{output}

### GENERATED TEST CASES

{tests}
"""

    return {"report": report}

# =====================================================
# BUILD LANGGRAPH
# =====================================================
workflow = StateGraph(CrewState)

workflow.add_node("developer", developer_node)
workflow.add_node("tester", tester_node)

workflow.add_edge(START, "developer")
workflow.add_edge("developer", "tester")
workflow.add_edge("tester", END)

graph = workflow.compile()

# =====================================================
# FASTAPI APP
# =====================================================
app = FastAPI(
    title="LangGraph Coding Assistant",
    version="1.0"
)

@app.get("/")
def home():
    return {"status": "LangGraph Agent Running Successfully 🚀"}

# =====================================================
# PLAYGROUND INPUT SCHEMA
# =====================================================
class TaskInput(BaseModel):
    task: str

# =====================================================
# PLAYGROUND RUNNER
# =====================================================
def run_agent(request: TaskInput):
    result = graph.invoke({
        "messages": [HumanMessage(content=request.task)]
    })

    return {
        "Generated Code": result["code"],
        "Execution Report": result["report"]
    }

playground_agent = RunnableLambda(run_agent).with_types(
    input_type=TaskInput
)

# Student Tribe Playground Route
add_routes(app, playground_agent, path="/agent")
