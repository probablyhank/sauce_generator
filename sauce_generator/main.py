from fastapi import FastAPI
from .big_brain import custom_prompt

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": custom_prompt(
            # enter your prompt
            "Write a sentence about a grumpy programmer named Henry."
        )
    }


@app.get("/prompt/{prompt}")
async def create_prompt(prompt):
    return {"output": custom_prompt(prompt)}
