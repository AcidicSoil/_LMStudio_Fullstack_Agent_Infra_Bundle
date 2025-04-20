from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from langchain.llms import OpenAI
from langchain.schema import HumanMessage
import os

# Initialize LLM from LM Studio
llm = OpenAI(
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"),
    openai_api_base=os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1"),
    model_name=os.getenv("OPENAI_MODEL_NAME", "mistral")
)

# Define reflection loop agent
def think_step(state):
    prompt = state.get("question", "")
    thought = llm.invoke(f"Think about this task: {prompt}")
    return {"thought": thought.content, "question": prompt, "iterations": state.get("iterations", 0) + 1}

def decide_step(state):
    decision = llm.invoke(f"Given your thought: '{state['thought']}', decide if more thinking is needed or give an answer.")
    if "final answer" in decision.content.lower():
        return {"response": decision.content, "done": True}
    else:
        return {"question": state["question"], "iterations": state["iterations"], "done": False}

# Define loop controller
def loop_control(state):
    return "Done" if state.get("done") else "Think"

# Wrap nodes
think = RunnableLambda(think_step)
decide = RunnableLambda(decide_step)

# Define LangGraph loop
graph = StateGraph(input_keys=["question"])
graph.add_node("Think", think)
graph.add_node("Decide", decide)
graph.add_conditional_edges("Decide", loop_control, {"Think": "Think", "Done": END})
graph.set_entry_point("Think")
graph.add_edge("Think", "Decide")

# Compile agent loop graph
app = graph.compile()