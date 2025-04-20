# PowerShell Script: setup_lmstudio_pipeline.ps1

Write-Host "Creating Python virtual environment..."
python -m venv venv
.\venv\Scripts\Activate.ps1

Write-Host "Installing core packages..."
pip install --upgrade pip
pip install langchain langgraph openai fastapi uvicorn

Write-Host "Installing LangGraph CUA and BigTool..."
pip install git+https://github.com/AcidicSoil/langgraph-cua-py.git
pip install git+https://github.com/langchain-ai/langgraph-bigtool.git

Write-Host "Cloning project repositories..."
git clone https://github.com/AcidicSoil/local-deep-researcher.git
git clone https://github.com/AcidicSoil/Adeep.git
git clone https://github.com/disler/indydevtools.git

Write-Host "Installing project requirements if available..."
foreach ($dir in @("local-deep-researcher", "Adeep", "indydevtools")) {
    $req = Join-Path $dir "requirements.txt"
    if (Test-Path $req) {
        pip install -r $req
    }
}

Write-Host "Setting LM Studio environment variables..."
@"
OPENAI_API_KEY=lm-studio
OPENAI_API_BASE=http://localhost:1234/v1
OPENAI_MODEL_NAME=mistral
"@ | Out-File -Encoding utf8 .env

Write-Host "Setup complete. Ensure LM Studio is running at localhost:1234."
