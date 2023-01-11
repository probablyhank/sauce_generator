from sqlalchemy.orm import Session
from .big_brain import custom_prompt, custom_rich_prompt, custom_filthy_rich_prompt

from . import models, schemas


def get_completion(db: Session, id: str):
    return db.query(models.Completion).filter(models.Completion.id == id).first()


def delete_completion(db: Session, id: str):
    completion_to_delete = db.query(models.Completion).filter(models.Completion.id == id).first()
    db.delete(completion_to_delete)
    db.commit()
    db.close()


def get_completions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Completion).offset(skip).limit(limit).all()


def get_completions_by_cost(db: Session, cost: int):
    return db.query(models.Completion).filter(models.Completion.total_cost <= cost).offset(0).limit(100).all()


def create_random_completion(db: Session):
    random_prompt = "Give me a random fact about absolutely anything."
    ada_model = "text-ada-001"
    openai_response = custom_prompt(random_prompt, ada_model)
    usage_obj = openai_response.usage
    db_completion = models.Completion(
        id=openai_response.id,
        model=ada_model,
        object=openai_response.object,
        prompt=random_prompt,
        output=openai_response.choices[0].text,
        prompt_cost=usage_obj.prompt_tokens,
        output_cost=usage_obj.completion_tokens,
    )
    db_completion.total_cost = db_completion.prompt_cost + db_completion.output_cost
    db.add(db_completion)
    db.commit()
    db.refresh(db_completion)
    return db_completion


def create_custom_completion(db: Session, c_prompt: str):
    ada_model = "text-ada-001"
    openai_response = custom_prompt(c_prompt, ada_model)
    usage_obj = openai_response.usage
    db_completion = models.Completion(
        id=openai_response.id,
        model=ada_model,
        object=openai_response.object,
        prompt=c_prompt,
        output=openai_response.choices[0].text,
        prompt_cost=usage_obj.prompt_tokens,
        output_cost=usage_obj.completion_tokens,
    )
    db_completion.total_cost = db_completion.prompt_cost + db_completion.output_cost
    db.add(db_completion)
    db.commit()
    db.refresh(db_completion)
    return db_completion


def create_rich_custom_completion(db: Session, c_prompt: str):
    ai_model = "text-davinci-003"
    openai_response = custom_rich_prompt(c_prompt, ai_model)
    usage_obj = openai_response.usage
    db_completion = models.Completion(
        id=openai_response.id,
        model=ai_model,
        object=openai_response.object,
        prompt=c_prompt,
        output=openai_response.choices[0].text,
        prompt_cost=usage_obj.prompt_tokens,
        output_cost=usage_obj.completion_tokens,
    )
    db_completion.total_cost = db_completion.prompt_cost + db_completion.output_cost
    db.add(db_completion)
    db.commit()
    db.refresh(db_completion)
    return db_completion


def create_filthy_rich_custom_completion(db: Session, c_prompt: str):
    ai_model = "text-davinci-003"
    openai_response = custom_filthy_rich_prompt(c_prompt, ai_model)
    usage_obj = openai_response.usage
    db_completion = models.Completion(
        id=openai_response.id,
        model=ai_model,
        object=openai_response.object,
        prompt=c_prompt,
        output=openai_response.choices[0].text,
        prompt_cost=usage_obj.prompt_tokens,
        output_cost=usage_obj.completion_tokens,
    )
    db_completion.total_cost = db_completion.prompt_cost + db_completion.output_cost
    db.add(db_completion)
    db.commit()
    db.refresh(db_completion)
    return db_completion
