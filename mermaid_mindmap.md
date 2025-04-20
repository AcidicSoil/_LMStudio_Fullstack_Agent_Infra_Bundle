graph TB
    ROOT[Modular AI Agent System (LM Studio)]

    ROOT --> LM[LM Studio (Quantized LLM Server)]
    ROOT --> LC[LangChain (Interface Layer)]
    LC --> LG[LangGraph (Execution Flows)]
    LG --> CUA[LangGraph-CUA (Reasoning Agents)]
    LG --> BIG[LangGraph-BigTool (Tool Use)]
    CUA --> ADEEP[Adeep (RAG + Agent Routing)]
    BIG --> ADEEP
    ADEEP --> MEM0[Mem0.ai (Vector Memory)]
    ADEEP --> RESEARCH[Local Deep Researcher]
    ADEEP --> DEVTOOLS[IndyDevTools (Code Panel)]
    ADEEP --> API[FastAPI / Streamlit (UI + API)]