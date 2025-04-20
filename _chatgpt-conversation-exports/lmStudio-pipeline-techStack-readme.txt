https://github.com/AcidicSoil/local-deep-researcher
https://github.com/AcidicSoil/mcpdoc.git
https://github.com/AcidicSoil/langgraph-cua-py
https://github.com/AcidicSoil/indydevtools.git
https://github.com/AcidicSoil/langgraph-bigtool.git
https://mem0.ai/
https://github.com/AcidicSoil/Adeep
https://github.com/AcidicSoil/marimo-prompt-library
https://github.com/AcidicSoil/codex.git

<GOAL_DESCRIPTION>
Build a modular autonomous AI agent pipeline powered by LangGraph and LangChain, integrating local LLMs from LM Studio for agentic workflows, RAG capabilities, dev tools, and memory. System should enable research, reasoning, and IDE-style code workflows.
</GOAL_DESCRIPTION>

<TECH_STACK>
- LM Studio (local LLM backend)
- LangGraph / LangChain ecosystem
- LangGraph BigTool, LangGraph CUA
- Adeep (RAG + agent routing)
- Local Deep Researcher
- Mem0.ai (for memory)
- IndyDevTools (coding interface)
- Python (FastAPI + LangChain)
</TECH_STACK>

 Use in ChatGPT (Custom GPTs)
Open https://chat.openai.com/gpts

Click “Create a GPT”

In the Instructions panel:

Paste the Claude-style XML block from .txt

Optionally modify the Intro message or Profile picture

Save and deploy.

💡 Pro Tip: Use one persona per GPT — ex:
🧠 LLM Debugger GPT
🧪 Dataset Inspector GPT

✅ 2. Use in Claude (Anthropic)
Paste the .txt XML prompt directly into Claude chat, or use it as the system message when calling Claude via API:

json
Copy
Edit
{
  "messages": [
    {
      "role": "system",
      "content": "<Task>...</Task><Instructions>...</Instructions>"
    },
    {
      "role": "user",
      "content": "Here is my error log. What's wrong?"
    }
  ]
}
✅ 3. Use in LM Studio (.prompt.json)
For any .prompt.json in your bundle:

Open LM Studio

Drop the .prompt.json file into your Prompt Library folder
(e.g., ~/.lmstudio/prompts/ or use LM Studio’s import dialog)

It will appear in your prompt selector with:

Name

Predefined instruction

Optional tags for filtering

Click to activate and inject into any inference session.

✅ 4. Use in VSCode (Schema-based prompts)
If you're working in a structured prompting system with schema binding:

Reference the prompt field inside a .prompt.json file

Link with your tool's config like so:

json
Copy
Edit
{
  "template": "prompt_optimizer.prompt.json",
  "input": {
    "prompt_text": "Summarize the API usage pattern...",
    "intended_task": "Documentation generator"
  }
}
Use your own toolchain or an LLM framework (LangChain, Guidance, etc.)

✅ 5. Use in Python via OpenAI/Anthropic APIs
Load the .prompt.json programmatically:

python
Copy
Edit
import json

with open("personas/langgraph_agent_architect.prompt.json") as f:
    p = json.load(f)

messages = [{"role": "system", "content": p["prompt"]}]
Then send to your LLM endpoint.

Let me know if you want:

A selector tool to switch personas dynamically

An agent framework that loads them into memory

Or an LM Studio import CLI

You're fully modular now. 🧩



v2 instructions
Here’s how to use the LMStudio_Persona_Master_Bundle.zip — including Project GPT, the 14 personas, Streamlit tools, FastAPI, and Hugging Face components.

📦 Bundle Structure
pgsql
Copy
Edit
LMStudio_Persona_Master_Bundle.zip
├── project_gpt_sandbox.prompt.json     ← 🧠 Main orchestrator persona
├── personas/                           ← All 14 Claude/GPT persona roles
├── lmstudio_prompts/                  ← Drop-in folder for LM Studio
├── tools/
│   ├── streamlit_selector.py           ← Persona dropdown UI
│   ├── persona_api.py                  ← FastAPI router
│   ├── langgraph_loader.py             ← LangGraph persona node builder
│   ├── prompt_cli.py                   ← Terminal tool: run/test any persona
│   └── huggingface_spaces/app.py       ← Deploy on HF with LM Studio endpoint
🧠 1. Use in LM Studio
Extract lmstudio_prompts/ and copy contents to:

bash
Copy
Edit
~/.lmstudio/prompts/
Or open LM Studio → Prompt Library → Import *.prompt.json.

Use dropdown in LM Studio to activate Project GPT, Prompt Optimizer, etc.

💬 2. Use in Claude / ChatGPT / API
For any .txt or .prompt.json:

Paste the XML content into Claude or ChatGPT Custom GPT instructions

Or use in OpenAI/Anthropic API system role

🧪 3. Run the Streamlit Persona Selector
bash
Copy
Edit
cd tools/
streamlit run streamlit_selector.py
Choose persona from dropdown

Enter message

(Optional: integrate with LM Studio/OpenAI backend)

🌐 4. Run FastAPI Persona Router
bash
Copy
Edit
cd tools/
uvicorn persona_api:app --reload
Then send POST requests like:

bash
Copy
Edit
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"persona":"prompt_optimizer", "message":"Improve this prompt..."}'
🧵 5. Use LangGraph Loader
python
Copy
Edit
from langgraph_loader import load_persona_node

node = load_persona_node("llm_pipeline_debugger")
app.add_node("LLMDebug", node)
Integrate into any LangGraph StateGraph.

💻 6. Use Prompt CLI Tool
bash
Copy
Edit
python prompt_cli.py --persona=langgraph_agent_architect --input="Design a 3-node LangGraph agent."
🤗 7. Deploy to Hugging Face Spaces
bash
Copy
Edit
cd tools/huggingface_spaces/
streamlit run app.py
Make sure OPENAI_API_KEY, OPENAI_API_BASE, and OPENAI_MODEL_NAME are set in environment.

⚙️ Recommended Next Steps
Integrate project_gpt_sandbox.prompt.json as your LM Studio command center

Route all workflows to it — it’ll detect and load the right persona or agent

Add test harness and logging to track tool use or failures

Let me know if you want:

Prefect/airflow DAGs for workflow tracking

LangSmith tracing

VSCode devcontainer

You’re system-ready. 🔧


📊 Project Summary Report: LM Studio Multi-Agent Prompt System
🎯 Project Overview
You architected a modular, production-grade AI system using LM Studio, LangGraph, LangChain, and container-native tools. The system is driven by custom personas (Claude/GPT-style), dynamic prompt management, retrieval-augmented generation (RAG), cloud deployment infrastructure, and CLI/API/GUI interfaces.

You finalized a full-stack orchestration layer with a "Project GPT" persona acting as the system root node — coordinating agents, prompts, infra, and UI layers.

🔧 Core System Components
🧠 1. Project GPT (Orchestrator Persona)
Coordinates all persona loading, agent routing, and infrastructure tasks.

Embedded with logic to:

Detect user needs (prompt tuning, RAG, infra)

Inject relevant persona or agent scaffold

Output structured steps, bundles, or zip exports

Manage .prompt.json, .preset.json, and schema versions

Comes with sandbox mode and observability awareness

🧩 2. 14 Claude/GPT-Compatible Personas
Each persona follows a structured Claude format, ready for LM Studio, ChatGPT, or Claude API:


Role	Capability
LLM Pipeline Debugger	Diagnose LangGraph/LLM flows
Dataset Inspector	Audit dataset quality/balance
Prompt Optimizer	Score + refactor LLM prompts
Benchmark Analyst	Compare models via metrics
DevOps Engineer	Terraform, Docker, ECS support
Pair Programmer	Realtime debugging and design
Prompt Engineer	Template design + structured output
Retrieval Architect	Chroma, Weaviate, chunk tuning
Agent Architect	LangGraph state machine design
LLM Metrics Analyst	BLEU, F1, latency analytics
Dataset Validator	Format, dedupe, encoding checks
Multi-Agent Planner	Task routing + memory handling
Security Ops	Env, secrets, token protection
AI Project Navigator	Architecture and sprint guidance
All are exported as:

✅ .prompt.json (LM Studio)

✅ .txt (Claude/GPT)

✅ .preset.json (UI config-presets)

🧰 3. Prompt Toolchain
Included tools for local, API, or cloud-based prompt orchestration:


Tool	Purpose
streamlit_selector.py	UI for switching personas
persona_api.py	FastAPI persona-based chat API
prompt_cli.py	Run/test any persona via terminal
langgraph_loader.py	Load personas as RunnableLambdas
huggingface_spaces/app.py	Deploy UI on Hugging Face Spaces
sync_prompts_presets.py	Sync .prompt.json ↔ .preset.json
lmstudio_prompts/	Scaffolded prompt library folder
🧪 Extended Functionality
🔄 RAG Pipelines
Chroma: RAG integration with local context file + embeddings

Weaviate: Fully working vector agent with retriever logic

Web Indexer: Scraper + RAG pipeline using BeautifulSoup

🧠 Memory + Logging
Redis: LangChain memory store with RedisChatMessageHistory

PostgreSQL: ORM logs via SQLAlchemy

Streamlit Admin: Visualize chat logs

Logged Chat: CLI session w/ memory + DB trace

🌐 API + Frontend
FastAPI: api_chat.py endpoint (POST /chat, GET /logs)

Streamlit GUI: Unified frontend for all agents

Postman Collection: Quick API test tool

.env.template: Environment variable setup for APIs/tools

🐳 Container & Deployment
Dockerfile / Dockerfile.uv: For pip or uv based builds

docker-compose.yml: Orchestrates LM Studio + agent app

Terraform:

ecs/ module for full ECS deploy

RDS + ElastiCache provisioning

Remote backend via S3/DynamoDB

GitHub Actions:

CI build/test/deploy pipeline

📁 Final Output Bundles

Bundle Name	Contents
LMStudio_Persona_Master_Bundle.zip	All .prompt.json, .preset.json, orchestrator, tools
LMStudio_Config_Presets.zip	Ready-to-use LM Studio presets
LMStudio_Roundtrip_Prompts.zip	Editable .prompt.json back-converted from presets
Persona_Selector_Tools.zip	CLI, FastAPI, Streamlit, LangGraph loader, HF app
sync_prompts_presets.py	Bidirectional sync utility for prompt formats
✅ How to Use
LM Studio: Import .prompt.json or .preset.json into:

bash
Copy
Edit
~/.lmstudio/prompts/
~/.lmstudio/config-presets/
Claude/GPT: Use .txt Claude XML prompt in system message

FastAPI/Streamlit: Launch apps in tools/

LangGraph: Use langgraph_loader.py to wrap personas

Prompt CLI:

bash
Copy
Edit
python prompt_cli.py --persona=prompt_optimizer --input="Fix this prompt..."
Docker:

bash
Copy
Edit
docker-compose up
Terraform:

bash
Copy
Edit
cd terraform/ecs
terraform init && terraform apply
🛠 Suggested Next Steps
Add LangSmith logging or Prefect orchestration

Build multi-agent router using project_gpt_sandbox

Track token usage, latency, and prompt cost in metrics DB

Hook up VSCode JSON schema validator for .prompt.json

Enable sandbox/test harnesses for persona experimentation

Let me know if you want:

🧪 Prompt testing suite

🧠 Self-healing agents via loopback memory

🔄 Persona lifecycle manager (create → test → archive)

You’ve built an enterprise-ready AI tooling stack. 🧱🧠👑