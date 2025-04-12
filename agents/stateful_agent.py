from llama_index.agent.openai import OpenAIAgent
from llama_index.llms import OpenAI

class StatefulAgent:
    def __init__(self):
        self.context = []
        self.llm = OpenAI(model='gpt-3.5-turbo')
        self.agent = OpenAIAgent.from_tools([], llm=self.llm, verbose=True)

    def chat(self, message):
        self.context.append(message)
        full_context = "\n".join(self.context)
        response = self.agent.chat(full_context)
        self.context.append(response.response)
        return response
