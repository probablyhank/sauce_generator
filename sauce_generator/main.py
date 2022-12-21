# TODO implement validation for model & throw exceptions for bad inputs
from fastapi import FastAPI, Query
from .big_brain import custom_prompt

app = FastAPI()


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
