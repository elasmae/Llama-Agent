from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms import OpenAI
from llama_index.agent import OpenAIAgent

def get_retrieval_agent():
    documents = SimpleDirectoryReader('data').load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    llm = OpenAI(model='gpt-3.5-turbo')
    agent = OpenAIAgent.from_tools([query_engine], llm=llm, verbose=True)
    return agent
