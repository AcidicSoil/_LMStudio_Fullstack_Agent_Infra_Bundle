import streamlit as st
from sqlalchemy import create_engine, text
import os
import pandas as pd

st.set_page_config(page_title="Chat Log Admin", layout="wide")
st.title("📜 Chat Log Viewer")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://dev:secret@localhost:5432/devdb")

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM chat_logs ORDER BY timestamp DESC LIMIT 100"))
    df = pd.DataFrame(result.fetchall(), columns=result.keys())

if df.empty:
    st.warning("No logs found.")
else:
    st.dataframe(df, use_container_width=True)