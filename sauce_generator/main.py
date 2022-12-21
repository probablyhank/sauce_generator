from fastapi import FastAPI
from .big_brain import custom_prompt

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to openAI via URL."}


@app.get("/prompt/{prompt}")
async def create_prompt(prompt):
    return {"output": custom_prompt(prompt)}
