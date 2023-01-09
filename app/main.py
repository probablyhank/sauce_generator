# TODO implement validation for model & throw exceptions for bad inputs
from typing import List
from fastapi import FastAPI, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .db import SessionLocal, engine
from .big_brain import custom_prompt

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_model(name):
    return f"text-{name}-001"


# more expensive, far richer results
davinci_model = "text-davinci-003"


@app.get("/")
async def root():
    return {"message": "Welcome to openAI via URL."}


@app.get("/prompt/{prompt}")
async def create_prompt(
    prompt: str,
    model=Query(
        default=create_model("ada"),
        description="change the middle value to 'ada', 'babbage', or 'curie'",
    ),
):
    return {"output": custom_prompt(prompt, model)}


@app.get("/completions")
async def read_all_completions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    completions = crud.get_completions(db, skip=skip, limit=limit)
    return completions


@app.post("/completions/create/random")
async def create_random_fact(db: Session = Depends(get_db)):
    comp = crud.create_random_completion(db)
    return comp


@app.post("/completions/create/custom/")
async def create_custom_completion(db: Session = Depends(get_db), prompt: str = "Give me facts about computers."):
    comp = crud.create_custom_completion(db, prompt)
    return comp


@app.post("/completions/create/custom-rich/")
async def create_custom_completion(db: Session = Depends(get_db), prompt: str = "Give me facts about computers."):
    comp = crud.create_rich_custom_completion(db, prompt)
    return comp
