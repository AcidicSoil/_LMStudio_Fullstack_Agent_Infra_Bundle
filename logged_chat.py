from langchain.memory import RedisChatMessageHistory
from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm_models import ChatLog, init_db
import os

# Setup Redis memory
history = RedisChatMessageHistory(
    url=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    session_id="chat-session-001"
)

# Setup LangChain LLM
llm = OpenAI(
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"),
    openai_api_base=os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1"),
    model_name=os.getenv("OPENAI_MODEL_NAME", "mistral")
)

# Setup DB
engine = init_db()
Session = sessionmaker(bind=engine)

# Setup LangChain ConversationChain
conversation = ConversationChain(llm=llm, memory=history)

# Chat + log loop
if __name__ == "__main__":
    session = Session()
    try:
        while True:
            user_input = input("You: ")
            if user_input.strip().lower() == "exit":
                break
            response = conversation.run(user_input)
            print("Assistant:", response)

            log = ChatLog(
                session_id="chat-session-001",
                user_message=user_input,
                assistant_response=response
            )
            session.add(log)
            session.commit()
    finally:
        session.close()