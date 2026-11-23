
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

customer = input("Name:")
rating = input("Rating:")
review = input("Review:")

prompt = f"""
Role:
    Act as a Restaurant General Manager
Task:
    Draft a responsive email to the customer review
    Customer Name: {customer}
    Rating : {rating}
    Review : {review}

Constraints:
    -Let it be a polite, courteouse response
    -Max 200 chars
    -if the rating is 4 or more, lets Thank for the rating.
    -if the rating is less than 4, address the issue and offer a solution
    -keep the email content unique every time

Output Format:
    Email Subject:
    Email Body:
    Regards:
    Dipeswar, 7601867358, Manager, CG Restaurant, Bengaluru

"""


# Make a request to the LLM model
response = llm.responses.create(
    model= os.getenv("OPENAI_MODEL"),
    input = prompt   
)

# print(response.usage)
# print('-'*30)
print(response.output_text)