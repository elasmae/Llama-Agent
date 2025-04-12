from llama_index.agent.openai import OpenAIAgent
from llama_index.llms import OpenAI
from tools.math_tools import add, subtract

def tool_add(a: int, b: int) -> str:
    return f"Result: {add(a, b)}"

def tool_subtract(a: int, b: int) -> str:
    return f"Result: {subtract(a, b)}"

def get_tools_agent():
    llm = OpenAI(model='gpt-3.5-turbo')
    tools = [tool_add, tool_subtract]
    agent = OpenAIAgent.from_tools(tools, llm=llm, verbose=True)
    return agent
