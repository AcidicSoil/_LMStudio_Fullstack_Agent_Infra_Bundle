from sqlalchemy import Column, Integer, String, DateTime, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://dev:secret@localhost:5432/devdb")
Base = declarative_base()

class ChatLog(Base):
    __tablename__ = "chat_logs"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(100), index=True)
    user_message = Column(Text)
    assistant_response = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

def init_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return engine

if __name__ == "__main__":
    engine = init_db()
    print("✅ PostgreSQL tables created.")