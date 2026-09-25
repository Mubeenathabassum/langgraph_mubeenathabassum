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

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in Render Environment Variables.")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key,
    temperature=0
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
    """Generate test cases using Gemini."""

    prompt = f"""
You are a Senior QA Engineer.

Generate 3-5 numbered test cases for this coding task:

{task_description}

Include edge cases also.
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
Write clean Python code for the following task.

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
### EXECUTION OUTPUT

{output}

### GENERATED TEST CASES

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
# FASTAPI + LANGSERVE
# =====================================================

app = FastAPI(
    title="LangGraph Coding Assistant",
    version="1.0"
)

@app.get("/")
def home():
    return {"status": "LangGraph Running Successfully 🚀"}

# Playground Input
class TaskInput(BaseModel):
    task: str

# Playground Output
class TaskOutput(BaseModel):
    generated_code: str
    execution_report: str

# Playground Runner
def agent_runner(data: TaskInput):

    result = graph.invoke({
        "messages": [HumanMessage(content=data.task)]
    })

    return TaskOutput(
        generated_code=result["code"],
        execution_report=result["report"]
    )

playground_agent = RunnableLambda(agent_runner).with_types(
    input_type=TaskInput,
    output_type=TaskOutput
)

# Student Tribe Playground
add_routes(app, playground_agent, path="/agent")
