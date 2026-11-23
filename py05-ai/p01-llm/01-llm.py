import os
from dotenv import load_dotenv
from openai import OpenAI


# Load configuration into from .env file
load_dotenv()

# Create an openai instance for api communication
llm = OpenAI()

# Make a request to the LLM model
response = llm.responses.create(
    model=os.getenv("OPENAI_MODEL"),
    input = "Explain LLM"
)

print(response.output_text)