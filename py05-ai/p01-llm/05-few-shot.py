
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

ticket = input("Enter the Issue: ")

prompt = f"""
Analyze the ticket and identify the issue, along with the urgency level as shown in the following examples

Input: My VM is not connecting even with the right credentials
Output: Defect : VM Connectivity        Urgency: High

Input: My mouse is not working.
Output: Defect : Mouse          Urgency: Low

Input: I am not able to install libraries in my machine
Output: Defect : Libraries Installation         Urgency: Medium

Review the below:
{ticket}
"""


# Make a request to the LLM model
response = llm.responses.create(
    model= os.getenv("OPENAI_MODEL"),
    input = prompt   
)

print(response.usage)
print('-'*30)
print(response.output_text)