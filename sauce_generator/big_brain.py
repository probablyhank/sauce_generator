import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# cheapest, simplest results
ada_model = "text-ada-001"
# medium cost & richness
babbage_model = "text-babbage-001"
# cheaper than davinci but still quite expensive
curie_model = "text-curie-001"
# more expensive, far richer results
davinci_model = "text-davinci-003"


def custom_prompt(cPrompt):
    cResponse = openai.Completion.create(
        model=ada_model,
        prompt=cPrompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0,
    )
    return cResponse
