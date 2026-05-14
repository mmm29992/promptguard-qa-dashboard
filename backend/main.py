from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(
    title="PromptGuard QA Dashboard API",
    description="API for testing AI prompts, tracking QA results, and logging defects.",
    version="1.0.0",
)

# Temporary in-memory storage for Day 1.
# Later, we will replace this with a real SQL database.
prompts = []


class PromptCreate(BaseModel):
    title: str
    prompt_text: str
    expected_behavior: str
    category: str


class Prompt(PromptCreate):
    id: int
    created_at: str


@app.get("/")
def root():
    return {
        "message": "Welcome to the PromptGuard QA Dashboard API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "PromptGuard API"
    }


@app.post("/prompts", response_model=Prompt)
def create_prompt(prompt: PromptCreate):
    new_prompt = {
        "id": len(prompts) + 1,
        "title": prompt.title,
        "prompt_text": prompt.prompt_text,
        "expected_behavior": prompt.expected_behavior,
        "category": prompt.category,
        "created_at": datetime.now().isoformat()
    }

    prompts.append(new_prompt)
    return new_prompt


@app.get("/prompts", response_model=List[Prompt])
def get_prompts():
    return prompts

@app.get("/prompts/{prompt_id}", response_model=Prompt)
def get_prompt_by_id(prompt_id: int):
    for prompt in prompts:
        if prompt["id"] == prompt_id:
            return prompt

    return {
        "id": 0,
        "title": "Not Found",
        "prompt_text": "No prompt found with that ID.",
        "expected_behavior": "N/A",
        "category": "Error",
        "created_at": datetime.now().isoformat()
    }