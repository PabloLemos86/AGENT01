from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI()

tasks = []

class Task(BaseModel):
    type: str
    command: str

@app.post("/task")
def create_task(task: Task):
    task_id = str(uuid.uuid4())
    tasks.append({
        "id": task_id,
        "type": task.type,
        "command": task.command,
        "status": "pending"
    })
    return {"task_id": task_id}

@app.get("/task")
def get_task():
    for task in tasks:
        if task["status"] == "pending":
            task["status"] = "processing"
            return task
    return {"status": "empty"}

@app.post("/task/{task_id}/complete")
def complete_task(task_id: str, result: dict):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["result"] = result
            return {"status": "completed"}
    return {"status": "not_found"}
