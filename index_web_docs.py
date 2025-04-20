import requests
from bs4 import BeautifulSoup
from langchain.document_loaders import Document
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os

# Function to extract clean text from a URL
def scrape_url(url):
    print(f"Scraping: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    text = soup.get_text(separator=" ", strip=True)
    return text

# Function to create Chroma vector index from scraped content
def index_urls(url_list, directory="chroma_store"):
    embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"))
    docs = []
    for url in url_list:
        content = scrape_url(url)
        docs.append(Document(page_content=content, metadata={"source": url}))
    vectordb = Chroma.from_documents(docs, embedding, persist_directory=directory)
    vectordb.persist()
    print("✅ Indexed all URLs.")

if __name__ == "__main__":
    urls = [
        "https://lmstudio.ai/docs/app",
        "https://github.com/langchain-ai/langgraph",
        "https://github.com/langchain-ai/langchain"
    ]
    index_urls(urls)