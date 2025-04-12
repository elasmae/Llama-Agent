from llama_index.agent.openai import OpenAIAgent
from llama_index.llms import OpenAI

def get_multi_agent():
    llm1 = OpenAI(model='gpt-3.5-turbo')
    llm2 = OpenAI(model='gpt-4')

    agent1 = OpenAIAgent.from_tools([], llm=llm1, verbose=True)
    agent2 = OpenAIAgent.from_tools([], llm=llm2, verbose=True)

    def collaborative_chat(message):
        response1 = agent1.chat(message)
        response2 = agent2.chat(response1.response)
        return response2

    return collaborative_chat
