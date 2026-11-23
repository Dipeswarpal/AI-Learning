

import os
from dotenv import load_dotenv
from openai import OpenAI


# Load configuration into from .env file
load_dotenv()

# Create an openai instance for api communication
# llm = OpenAI()
llm = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

# Make a request to the LLM model
response = llm.responses.create(
    model= os.getenv("OPENAI_MODEL"),

    instructions = "Act as a chef, Summerise the folloywing in bullet points",
    temperature = 0.7,
    max_output_tokens = 200,

    input = "Ingredients for Veg Pulao."
    
)

print(response.usage)
print('-'*30)
print(response.output_text)