import os
import uvicorn
import io
import sys
import traceback

from fastapi import FastAPI
from langserve import add_routes
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field
from typing import TypedDict, List, Optional

# =====================================================
# GEMINI MODEL
# =====================================================

GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in Render Environment Variables.")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0
)

# =====================================================
# STATE
# =====================================================

class CrewState(TypedDict):
    messages: List
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
    """Generate 3-5 test cases for a coding problem."""

    prompt = f"""
You are a Senior QA Engineer.

Generate 3-5 numbered test cases for this coding task.

Task:
{task_description}

Include edge cases.
"""

    response = llm.invoke(prompt)
    return str(response.content)

# =====================================================
# DEVELOPER NODE
# =====================================================

def developer_node(state: CrewState):

    task = state["messages"][-1].content

    prompt = f"""
Write clean Python code for this task.

Task:
{task}

Return ONLY Python code.
"""

    response = llm.invoke(prompt)

    code = str(response.content)
    code = code.replace("```python", "").replace("```", "").strip()

    return {"code": code}

# =====================================================
# TESTER NODE
# =====================================================

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

# =====================================================
# LANGGRAPH WORKFLOW
# =====================================================

workflow = StateGraph(CrewState)

workflow.add_node("developer", developer_node)
workflow.add_node("tester", tester_node)

workflow.add_edge(START, "developer")
workflow.add_edge("developer", "tester")
workflow.add_edge("tester", END)

graph = workflow.compile()

# =====================================================
# LANGSERVE INPUT / OUTPUT
# =====================================================

class AgentInput(BaseModel):
    input: str = Field(description="Enter your coding task.")

def format_input(data):
    user_input = data["input"] if isinstance(data, dict) else data.input
    return {
        "messages": [HumanMessage(content=user_input)]
    }

def extract_output(state):
    return {
        "generated_code": state["code"],
        "execution_report": state["report"]
    }

formatted_graph_chain = (
    RunnableLambda(format_input)
    | graph
    | RunnableLambda(extract_output)
).with_types(input_type=AgentInput)

# =====================================================
# FASTAPI APP
# =====================================================

app = FastAPI(title="LangGraph Coding Assistant")

add_routes(app, formatted_graph_chain, path="/agent")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
