#!/bin/bash

# Set up environment for LM Studio + LangChain + LangGraph system using uv

echo "Installing uv package manager..."
curl -LsSf https://astral.sh/uv/install.sh | sh

echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing core packages with uv..."
uv pip install --upgrade pip
uv pip install -r requirements.txt

echo "Cloning project repositories..."
git clone https://github.com/AcidicSoil/local-deep-researcher.git
git clone https://github.com/AcidicSoil/Adeep.git
git clone https://github.com/disler/indydevtools.git

echo "Installing requirements for each project (if present)..."
for dir in local-deep-researcher Adeep indydevtools; do
  if [ -f "$dir/requirements.txt" ]; then
    uv pip install -r "$dir/requirements.txt"
  fi
done

echo "Setting LM Studio environment variables..."
cat <<EOF > .env
OPENAI_API_KEY=lm-studio
OPENAI_API_BASE=http://localhost:1234/v1
OPENAI_MODEL_NAME=mistral
EOF

echo "Environment setup complete. Ensure LM Studio is running at localhost:1234."