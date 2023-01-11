from pydantic import BaseModel


class CompletionBase(BaseModel):
    model: str


# TODO add a new model for random completions that take no model or prompt


class CompletionCreate(CompletionBase):
    prompt: str


class Completion(CompletionBase):
    id: str
    prompt: str
    object: str
    output: str
    prompt_cost: int
    output_cost: int
    total_cost: int

    class Config:
        orm_mode = True
