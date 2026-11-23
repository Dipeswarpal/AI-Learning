
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

# customer = input("Name:")
# rating = input("Rating:")
# review = input("Review:")
prompt = """
You are an experienced Python corporate trainer.
 
Task:
Explain exception handling in Python to a beginner.
 
Instructions:
1. Explain what an exception is.
2. Explain why exception handling is important.
3. Explain try, except, else, and finally.
4. Provide a real-world ATM withdrawal example.
5. Include a simple Python code example.
6. Explain the code in beginner-friendly language.
7. Ask one interview question at the end.
 
Constraints:
- Use simple English.
- Avoid unnecessary technical jargon.
- Keep the explanation practical.
- Use plain text formatting.
"""

with llm.responses.stream( model = os.getenv("OPENAI_MODEL"), input = prompt) as stream:
    for event in stream:
        if event.type == "response.output_text.delta" :
            print(event.delta, end="", flush = True)