from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.llms import OpenAI
import os

# Init LM Studio-backed LLM
llm = OpenAI(
    temperature=0.4,
    openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"),
    openai_api_base=os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1"),
    model_name=os.getenv("OPENAI_MODEL_NAME", "mistral")
)

# Set up conversation memory
memory = ConversationBufferMemory(return_messages=True)

# Define two LangGraph agent nodes with reasoning
def planner_node(state):
    q = state.get("question", "")
    prompt = f"Analyze the user's request and decide a plan: '{q}'"
    plan = llm.invoke(prompt)
    return {"plan": plan.content, "question": q}

def executor_node(state):
    question = state.get("question", "")
    plan = state.get("plan", "")
    response = llm.invoke(f"Given the plan '{plan}', answer the question: {question}")
    return {"response": response.content}

# Wrap nodes
planner = RunnableLambda(planner_node)
executor = RunnableLambda(executor_node)

# LangGraph assembly
graph = StateGraph(input_keys=["question"])
graph.add_node("Planner", planner)
graph.add_node("Executor", executor)
graph.add_edge("Planner", "Executor")
graph.set_entry_point("Planner")
graph.set_finish_point("Executor", END)

# Compile graph
app = graph.compile()