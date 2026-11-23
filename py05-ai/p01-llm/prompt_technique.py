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

class PromptTechnique:

    def ask(self, prompt):
        response = llm.responses.create(
            model = os.getenv("OPENAI_MODEL"),
            temperature=0.7,
            input = prompt
        )

        print("------------------------")
        print(response.output_text)
        print("------------------------")