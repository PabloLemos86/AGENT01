# Agent Render Project

## 1. Instalar dependências

pip install -r requirements.txt

## 2. Definir variável de ambiente

Linux/Mac:
export GEMINI_API_KEY="SUA_CHAVE_AQUI"

Windows:
set GEMINI_API_KEY=SUA_CHAVE_AQUI

## 3. Executar localmente

uvicorn app.main:app --host 0.0.0.0 --port 8000

Acesse:
http://localhost:8000/docs

## 4. Deploy no Render

Build Command:
pip install -r requirements.txt

Start Command:
uvicorn app.main:app --host 0.0.0.0 --port 10000

Variável de ambiente:
GEMINI_API_KEY=SUA_CHAVE_AQUI
