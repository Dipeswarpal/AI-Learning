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
    input = "Capital of India?"
)

print(response.output_text)