from fastapi import FastAPI
from langchain.llms import OpenAI
import os

app = FastAPI()

# Load env config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "lm-studio")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1")
OPENAI_MODEL = os.getenv("OPENAI_MODEL_NAME", "mistral")

llm = OpenAI(
    temperature=0.3,
    openai_api_key=OPENAI_API_KEY,
    openai_api_base=OPENAI_API_BASE,
    model_name=OPENAI_MODEL
)

@app.get("/")
def read_root():
    return {"message": "LM Studio AI API is live."}

@app.get("/ask")
def ask(question: str):
    return {"response": llm(question)}