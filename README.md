# 🧠 LM Studio LLM Agent Stack

This repo contains a full-featured LLM agent framework powered by **LM Studio**, **LangChain**, and **LangGraph**. It integrates:

- 🔁 LangChain memory (Redis)
- 🗃️ PostgreSQL logging (via SQLAlchemy)
- 🌐 Streamlit UI and FastAPI endpoints
- 🧪 Docker, Compose, and CI-ready setup
- 📦 uv-based fast Python installs
- 📬 Postman collection for API testing

---

## 🔧 Quickstart

```bash
# Clone and configure
cp .env.template .env
docker-compose -f docker-compose.db.yml up --build
```

---

## 🚀 Streamlit Apps

| File | Description |
|------|-------------|
| `streamlit_app.py` | Run LangGraph agents in a GUI |
| `streamlit_admin.py` | View PostgreSQL chat logs |

Launch with:

```bash
streamlit run streamlit_app.py
```

---

## 💬 FastAPI Endpoints

Run:

```bash
uvicorn api_chat:app --reload
```

### POST `/chat`

```json
{ "message": "What is LangGraph?" }
```

### GET `/logs`

Returns recent chat history.

---

## 🧱 Redis + Postgres Integration

- Redis memory via `RedisChatMessageHistory`
- Chat logs stored in PostgreSQL table `chat_logs`

---

## 📬 API Testing

Import `lmstudio_chat_api.postman_collection.json` into Postman or Insomnia.

---

## 🐳 Docker Stack

- LM Studio (LLM inference)
- Redis
- PostgreSQL
- LangChain + LangGraph + Streamlit/LLM UI

```bash
docker-compose -f docker-compose.db.yml up
```

---

## 🛠 Developer Scripts

| File | Description |
|------|-------------|
| `setup_lmstudio_pipeline_uv.sh` | Bash setup using `uv` |
| `setup_lmstudio_pipeline_uv.ps1` | PowerShell setup using `uv` |
| `logged_chat.py` | CLI chat with Redis + Postgres |
| `orm_models.py` | SQLAlchemy DB models |
| `redis_memory_chat.py` | LangChain + Redis session |
| `api_chat.py` | FastAPI endpoints for LLM interface |

---

## 📦 Included Prompt Files

| File | Use |
|------|-----|
| `claude_prompt.txt` | Claude system prompt |
| `chatgpt_prompt.txt` | ChatGPT prompt |
| `llm_output_schema.json` | JSON schema for LLM outputs |

---

## 👷 GitHub Actions

CI via `.github/workflows/ci.yml`

---

## 🔐 Env Setup

Copy the `.env.template` to `.env` and update:

```dotenv
OPENAI_API_KEY=lm-studio
OPENAI_API_BASE=http://localhost:1234/v1
OPENAI_MODEL_NAME=mistral
DATABASE_URL=postgresql://dev:secret@localhost:5432/devdb
REDIS_URL=redis://localhost:6379/0
```

---

## 🧪 Test + Validate

```bash
python logged_chat.py
streamlit run streamlit_admin.py
uvicorn api_chat:app
```

---

## ✅ Done

This system is modular, testable, and cloud-ready.