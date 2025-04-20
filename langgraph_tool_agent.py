from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from langchain.llms import OpenAI
import os

# Initialize LLM from LM Studio
llm = OpenAI(
    temperature=0.2,
    openai_api_key=os.getenv("OPENAI_API_KEY", "lm-studio"),
    openai_api_base=os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1"),
    model_name=os.getenv("OPENAI_MODEL_NAME", "mistral")
)

# Define a tool execution step (insecure eval for local experiments only)
def run_python_tool(state):
    code = state.get("code_snippet", "")
    try:
        exec_globals = {}
        exec(code, exec_globals)
        output = exec_globals.get("result", "Executed (no result)")
    except Exception as e:
        output = f"Error: {e}"
    return {"tool_output": output}

# Define LLM node to generate Python code
def generate_code(state):
    question = state.get("question", "")
    prompt = f"Write Python code to solve this: {question}
Return it in a variable called `result`."
    response = llm.invoke(prompt)
    return {"code_snippet": response.content, "question": question}

# Wrap nodes
gen_code = RunnableLambda(generate_code)
exec_code = RunnableLambda(run_python_tool)

# Assemble LangGraph
graph = StateGraph(input_keys=["question"])
graph.add_node("CodeGen", gen_code)
graph.add_node("Execute", exec_code)
graph.add_edge("CodeGen", "Execute")
graph.set_entry_point("CodeGen")
graph.set_finish_point("Execute", END)

# Compile
app = graph.compile()