from pydantic import BaseModel


class CostBase(BaseModel):
    completion_id: str


class CostCreate(CostBase):
    prompt_cost: int
    output_cost: int


class Cost(CostBase):
    prompt_cost: int
    output_cost: int
    total_cost = prompt_cost + output_cost

    class Config:
        orm_mode = True


class CompletionBase(BaseModel):
    model: str


class CompletionCreate(CompletionBase):
    prompt: str


class Completion(CompletionBase):
    id: str
    object: str
    output: str
    usage: list[Cost] = []

    class Config:
        orm_mode = True
