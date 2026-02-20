from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import run_agent

app = FastAPI()

class RequestModel(BaseModel):
    message: str

@app.post("/chat")
def chat(request: RequestModel):
    return run_agent(request.message)
