
import os
import json
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
I am Rajesh Kumar,
MCA graduate with 15 years of experience
in python, django, flask, ai akills.

"""
instructions = """
Act as a HR Manager and analyze the following resume and 
return name, experience, qualification, skills, score and recommendation

Output Format:
- Json
- Remove the prefix '''json and suffix'''
"""


# Make a request to the LLM model
response = llm.responses.create(
    model= os.getenv("OPENAI_MODEL"),
    instructions = instructions,
    input = prompt   
)

# print(response.usage)
# print('-'*30)
print(response.output_text)