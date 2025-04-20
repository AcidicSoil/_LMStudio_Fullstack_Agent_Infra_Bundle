from langchain.memory import RedisChatMessageHistory
from langchain.chains import ConversationChain
from langchain.llms import OpenAI
import os

# Setup Redis history
history = RedisChatMessageHistory(
    url=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    session_id="chat-session-001"
)

# Setup LLM (LM Studio OpenAI-compatible)
llm = OpenAI(
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"),
    openai_api_base=os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1"),
    model_name=os.getenv("OPENAI_MODEL_NAME", "mistral")
)

# Setup conversation chain with memory
conversation = ConversationChain(
    llm=llm,
    memory=history,
    verbose=True
)

# Example use
if __name__ == "__main__":
    while True:
        msg = input("You: ")
        if msg.strip().lower() == "exit":
            break
        response = conversation.run(msg)
        print("Assistant:", response)