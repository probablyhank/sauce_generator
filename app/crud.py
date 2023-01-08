from sqlalchemy.orm import Session
from .big_brain import custom_prompt

from . import models, schemas


def get_completion(db: Session, id: str):
    return db.query(models.Completion).filter(models.Completion.id == id).first()


def get_completions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Completion).offset(skip).limit(limit).all()


def get_completions_by_cost(db: Session, cost: int):
    return db.query(models.Completion).filter(models.Completion.usage.total_cost <= cost).offset(0).limit(100).all()


# integrate openai completions into this create method
def create_completion(db: Session, completion: schemas.CompletionCreate):
    completion = schemas.CompletionCreate(model="test", prompt="test")
    db.add(completion)
    db.commit()
    db.refresh(completion)
    return completion
