graph LR
    A[LM Studio (LLM Inference)]
    B[LangChain]
    C[LangGraph (CUA / BigTool)]
    D[Adeep (RAG + Agent Orchestration)]
    E[Local Deep Researcher]
    F[Mem0.ai (Memory API)]
    G[IndyDevTools (Coding Interface)]
    H[FastAPI / Frontend]

    A -->|OpenAI API-compatible| B
    B --> C
    C --> D
    D --> E
    D --> F
    D --> G
    D --> H