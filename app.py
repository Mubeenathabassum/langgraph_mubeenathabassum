from fastapi import FastAPI
from pydantic import BaseModel
from typing import TypedDict, List, Optional
import os, io, sys, traceback
from langchain_core.messages import HumanMessage, BaseMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
api_key=os.getenv('GEMINI_API_KEY')
llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash',google_api_key=api_key)
app=FastAPI(title='LangGraph Coding Agent')
class TaskRequest(BaseModel):
    task:str
class CrewState(TypedDict):
    messages:List[BaseMessage]; code:Optional[str]; report:Optional[str]
@tool
def run_python_code(code:str)->str:
    clean=code.replace('```python','').replace('```','').strip(); old=sys.stdout; buf=io.StringIO(); sys.stdout=buf
    try:
        exec(clean,{"__builtins__":__builtins__},{}); out=buf.getvalue() or 'Success (No Output)'
    except Exception:
        out=traceback.format_exc()
    finally:
        sys.stdout=old
    return out
@tool
def generate_test_cases(task_description:str)->str:
    return llm.invoke(f'Generate 3-5 numbered test cases for: {task_description}').content

def developer_node(state:CrewState):
    task=state['messages'][-1].content
    code=llm.invoke(f'Write Python code only for: {task}').content.replace('```python','').replace('```','').strip(); return {'code':code}

def tester_node(state:CrewState):
    tests=generate_test_cases.invoke(state['messages'][-1].content); out=run_python_code.invoke({'code':state['code']}); return {'report':f'Execution Output\n{out}\n\nGenerated Test Cases\n{tests}'}
workflow=StateGraph(CrewState); workflow.add_node('developer',developer_node); workflow.add_node('tester',tester_node); workflow.add_edge(START,'developer'); workflow.add_edge('developer','tester'); workflow.add_edge('tester',END); graph=workflow.compile()
@app.get('/')
def home(): return {'status':'LangGraph API Running on Render'}
@app.post('/generate')
def generate_solution(request:TaskRequest):
    result=graph.invoke({'messages':[HumanMessage(content=request.task)]}); return {'task':request.task,'generated_code':result['code'],'report':result['report']}
