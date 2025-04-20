import streamlit as st
from langgraph_agent_app import app as agent_app
from langgraph_loop_agent import app as loop_app
from langgraph_tool_agent import app as tool_app

st.set_page_config(page_title="LM Studio AI Agents", layout="wide")
st.title("🧠 Modular AI Agents — LM Studio")

# User input
query = st.text_input("Ask a question", "")

# Agent selection
agent_type = st.selectbox("Select Agent Type", ["Planner + Executor", "Loop (ReAct)", "Tool Execution"])

# Trigger
if st.button("Run Agent") and query:
    with st.spinner("Running..."):
        if agent_type == "Planner + Executor":
            result = agent_app.invoke({"question": query})
            st.subheader("Response")
            st.text(result["response"])
        elif agent_type == "Loop (ReAct)":
            result = loop_app.invoke({"question": query})
            st.subheader("Response")
            st.text(result["response"])
        elif agent_type == "Tool Execution":
            result = tool_app.invoke({"question": query})
            st.subheader("Tool Output")
            st.text(result["tool_output"])