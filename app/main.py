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


default_string = "Give me 5 facts about RESTful APIs"


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


@app.get("/completions/{comp_id}")
async def read_completion_by_id(comp_id: str, db: Session = Depends(get_db)):
    db_comp = crud.get_completion(db, id=comp_id)
    if db_comp is None:
        raise HTTPException(status_code=404, detail="No completion with this ID was found.")
    return db_comp


# TODO sort return by total cost values
@app.get("/completion/cost/{total_cost}")
async def get_completions_by_cost(total_cost: int, db: Session = Depends(get_db)):
    completions_by_cost = crud.get_completions_by_cost(db, cost=total_cost)
    if len(completions_by_cost) < 1:
        raise HTTPException(status_code=404, detail="There are no completions in this cost range.")
    return completions_by_cost


@app.get("/completions")
async def read_all_completions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    completions = crud.get_completions(db, skip=skip, limit=limit)
    return completions


@app.post("/completions/create/random")
async def create_random_fact(db: Session = Depends(get_db)):
    comp = crud.create_random_completion(db)
    return comp


@app.post("/completions/create/custom")
async def create_custom_completion(db: Session = Depends(get_db), prompt: str = default_string):
    comp = crud.create_custom_completion(db, prompt)
    return comp


@app.post("/completions/create/custom-rich")
async def create_rich_custom_completion(db: Session = Depends(get_db), prompt: str = default_string):
    comp = crud.create_rich_custom_completion(db, prompt)
    return comp


@app.post("/completions/create/custom-filthy-rich")
async def create_filthy_rich_custom_completion(db: Session = Depends(get_db), prompt: str = default_string):
    comp = crud.create_filthy_rich_custom_completion(db, prompt)
    return comp


@app.delete("/delete/completions/{comp_id}")
async def delete_completion(id: str, db: Session = Depends(get_db)):
    comp_to_delete = crud.get_completion(db, id)
    if not comp_to_delete:
        raise HTTPException(status_code=404, detail="Completion was not found.  No data was deleted.")
    crud.delete_completion(db, id)
    return {"response": "Completion was sucessfully deleted."}
