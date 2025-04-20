#!/bin/bash

# Set up environment for LM Studio + LangChain + LangGraph system

echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing core packages..."
pip install --upgrade pip
pip install langchain langgraph openai fastapi uvicorn

echo "Installing LangGraph CUA and BigTool..."
pip install git+https://github.com/AcidicSoil/langgraph-cua-py.git
pip install git+https://github.com/langchain-ai/langgraph-bigtool.git

echo "Cloning project repositories..."
git clone https://github.com/AcidicSoil/local-deep-researcher.git
git clone https://github.com/AcidicSoil/Adeep.git
git clone https://github.com/disler/indydevtools.git

echo "Installing project requirements (if present)..."
for dir in local-deep-researcher Adeep indydevtools; do
  if [ -f "$dir/requirements.txt" ]; then
    pip install -r "$dir/requirements.txt"
  fi
done

echo "Setting environment variables for LM Studio..."
cat <<EOF > .env
OPENAI_API_KEY=lm-studio
OPENAI_API_BASE=http://localhost:1234/v1
OPENAI_MODEL_NAME=mistral
EOF

echo "Environment setup complete. Ensure LM Studio is running at localhost:1234."
