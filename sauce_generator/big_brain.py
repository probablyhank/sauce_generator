# TODO: Add openAI code
import os
import openai
from dotenv import load_dotenv

load_dotenv()

# replace this value with your personal openai api key
openai.api_key = os.getenv("OPENAI_API_KEY")


def custom_prompt(cPrompt):
    cResponse = openai.Completion.create(
        model="text-ada-001",
        prompt=cPrompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0,
    )
    return cResponse
