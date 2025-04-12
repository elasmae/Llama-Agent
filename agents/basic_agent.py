from llama_index.agent.openai import OpenAIAgent
from llama_index.llms import OpenAI

def get_basic_agent():
    llm = OpenAI(model='gpt-3.5-turbo')
    agent = OpenAIAgent.from_tools([], llm=llm, verbose=True)
    return agent
