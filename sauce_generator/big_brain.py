import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def custom_prompt(c_prompt, c_model):
    c_response = openai.Completion.create(
        model=c_model,
        prompt=c_prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=2.0,
        presence_penalty=1.0,
    )
    return c_response
