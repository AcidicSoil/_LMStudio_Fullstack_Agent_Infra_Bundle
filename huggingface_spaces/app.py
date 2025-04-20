import streamlit as st
from langgraph_rag_agent import app as rag_app

st.set_page_config(page_title="LM Studio RAG Agent", layout="wide")
st.title("🧠 Retrieval-Augmented LLM Agent (Chroma + LangGraph)")

query = st.text_input("Ask a question:")

if st.button("Submit") and query:
    response = rag_app.invoke({"question": query})
    st.success(response["response"])