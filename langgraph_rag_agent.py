from langgraph.graph import StateGraph, END
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
import os

# Setup embedding + LLM
embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"))
llm = OpenAI(
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"),
    openai_api_base=os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1"),
    model_name=os.getenv("OPENAI_MODEL_NAME", "mistral")
)

# Load and index documents
def init_chroma():
    loader = TextLoader("docs/context.txt")  # example file
    docs = loader.load()
    vectordb = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory="chroma_store")
    vectordb.persist()
    return vectordb

# Node: run RAG retrieval
def retrieve_node(state):
    db = Chroma(persist_directory="chroma_store", embedding_function=embedding)
    retriever = db.as_retriever()
    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    result = rag_chain.run(state.get("question", ""))
    return {"response": result}

# LangGraph setup
from langchain_core.runnables import RunnableLambda
retrieval = RunnableLambda(retrieve_node)

graph = StateGraph(input_keys=["question"])
graph.add_node("RAG", retrieval)
graph.set_entry_point("RAG")
graph.set_finish_point("RAG", END)

app = graph.compile()

if __name__ == "__main__":
    # Bootstrap if needed
    if not os.path.exists("chroma_store/index"):
        init_chroma()
    print(app.invoke({"question": "What is this system about?"}))