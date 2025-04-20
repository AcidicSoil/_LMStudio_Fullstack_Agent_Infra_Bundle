from langchain.vectorstores import Weaviate
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from weaviate.client import Client
import os

# Connect to Weaviate instance (must be running separately)
WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://localhost:8080")

client = Client(WEAVIATE_URL)
embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"))
llm = OpenAI(
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"),
    openai_api_base=os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1"),
    model_name=os.getenv("OPENAI_MODEL_NAME", "mistral")
)

db = Weaviate(client=client, embedding=embedding, index_name="Docs")
retriever = db.as_retriever()
rag = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

if __name__ == "__main__":
    query = input("Ask your RAG agent: ")
    result = rag.run(query)
    print("Answer:", result)