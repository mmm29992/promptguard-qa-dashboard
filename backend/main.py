from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional

from database import engine, SessionLocal, Base
from models import Prompt


Base.metadata.create_all(bind=engine)

app = FastAPI()


class PromptCreate(BaseModel):
    title: str
    content: str
    expected_result: Optional[str] = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Welcome to the PromptGuard QA Dashboard API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/prompts")
def create_prompt(prompt: PromptCreate, db: Session = Depends(get_db)):
    new_prompt = Prompt(
        title=prompt.title,
        content=prompt.content,
        expected_result=prompt.expected_result
    )

    db.add(new_prompt)
    db.commit()
    db.refresh(new_prompt)

    return new_prompt


@app.get("/prompts")
def get_prompts(db: Session = Depends(get_db)):
    prompts = db.query(Prompt).all()
    return prompts


@app.get("/prompts/{prompt_id}")
def get_prompt(prompt_id: int, db: Session = Depends(get_db)):
    prompt = db.query(Prompt).filter(Prompt.id == prompt_id).first()

    if prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")

    return prompt