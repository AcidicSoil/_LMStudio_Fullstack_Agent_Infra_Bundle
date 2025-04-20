from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.llms import OpenAI
from langchain.memory import RedisChatMessageHistory
from langchain.chains import ConversationChain
from sqlalchemy.orm import sessionmaker
from orm_models import ChatLog, init_db
import os

app = FastAPI()

# Setup Redis memory and SQLAlchemy
history = RedisChatMessageHistory(
    url=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    session_id="api-session"
)

llm = OpenAI(
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"),
    openai_api_base=os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1"),
    model_name=os.getenv("OPENAI_MODEL_NAME", "mistral")
)

conversation = ConversationChain(llm=llm, memory=history)
engine = init_db()
Session = sessionmaker(bind=engine)

class MessageInput(BaseModel):
    message: str

@app.post("/chat")
def chat_with_llm(payload: MessageInput):
    session = Session()
    try:
        user_input = payload.message
        response = conversation.run(user_input)

        log = ChatLog(
            session_id="api-session",
            user_message=user_input,
            assistant_response=response
        )
        session.add(log)
        session.commit()

        return {"response": response}
    finally:
        session.close()

@app.get("/logs")
def get_logs():
    session = Session()
    try:
        logs = session.query(ChatLog).order_by(ChatLog.timestamp.desc()).limit(100).all()
        return [
            {
                "user_message": log.user_message,
                "assistant_response": log.assistant_response,
                "timestamp": log.timestamp.isoformat()
            } for log in logs
        ]
    finally:
        session.close()