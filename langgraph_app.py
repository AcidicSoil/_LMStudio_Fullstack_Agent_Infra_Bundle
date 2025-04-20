from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from langchain.schema import SystemMessage, HumanMessage
from langchain.llms import OpenAI
import os

# Initialize OpenAI-compatible LLM via LM Studio
llm = OpenAI(
    temperature=0.2,
    openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"),
    openai_api_base=os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1"),
    model_name=os.getenv("OPENAI_MODEL_NAME", "mistral")
)

# Define basic LangGraph node
def respond_node(state):
    input_text = state.get("question", "")
    output = llm.invoke([SystemMessage(content="You are a helpful assistant."),
                         HumanMessage(content=input_text)])
    return {"response": output.content}

# Register node with LangGraph
respond = RunnableLambda(respond_node)

# Define LangGraph state graph
graph = StateGraph(input_keys=["question"])
graph.add_node("LLM_Respond", respond)
graph.set_entry_point("LLM_Respond")
graph.set_finish_point("LLM_Respond", END)

# Compile to executable app
app = graph.compile()