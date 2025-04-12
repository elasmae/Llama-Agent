from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.llms import OpenAI
from llama_index.agent import OpenAIAgent

def get_chroma_agent():
    documents = SimpleDirectoryReader('data').load_data()
    vector_store = ChromaVectorStore(persist_dir="chroma_store")
    index = VectorStoreIndex.from_documents(documents, vector_store=vector_store)
    query_engine = index.as_query_engine()

    llm = OpenAI(model='gpt-3.5-turbo')
    agent = OpenAIAgent.from_tools([query_engine], llm=llm, verbose=True)
    return agent
