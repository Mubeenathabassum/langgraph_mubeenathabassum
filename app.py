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
# GEMINI MODEL
# =====================================================
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key,
    temperature=0
)

# =====================================================
# GRAPH STATE
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
    """Generate 3-5 test cases."""

    prompt = f"""
You are a Senior QA Engineer.

Generate 3-5 numbered test cases for this coding task.

Task:
{task_description}

Include edge cases.
"""

    response = llm.invoke(prompt)

    if isinstance(response.content, list):
        return "".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for part in response.content
        )

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

    if isinstance(response.content, list):
        code = "".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for part in response.content
        )
    else:
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
app = FastAPI(title="LangGraph Coding Assistant")

@app.get("/")
def home():
    return {"status": "LangGraph Running Successfully"}

# =====================================================
# PLAYGROUND INPUT / OUTPUT
# =====================================================
class TaskInput(BaseModel):
    task: str

class TaskOutput(BaseModel):
    generated_code: str
    execution_report: str

# =====================================================
# LANGSERVE PLAYGROUND RUNNER
# =====================================================
def playground_runner(data: dict):

    result = graph.invoke(
        {
            "messages": [HumanMessage(content=data["task"])]
        }
    )

    return {
        "generated_code": result["code"],
        "execution_report": result["report"]
    }

playground_agent = RunnableLambda(playground_runner).with_types(
    input_type=TaskInput,
    output_type=TaskOutput
)

# IMPORTANT: This creates /agent/playground
add_routes(app, playground_agent, path="/agent")
