 
import os
from typing import Optional
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
 
load_dotenv()
 
print("dotenv loaded")
 
llm = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)
 
class ResumeAnalysis(BaseModel):
    name:str
    experience: int = 1
    qualification: Optional[str]
    skills: list[str]
    score: float
    recommendation: str
 
prompt = """
I am Gayathri,
MCA graduate with 14 years of experience
in python, django, flask, ai skills """
 
instructions = "Act as a HR Manager and analyze the following resume"
 
response = llm.responses.parse(
    model=os.getenv("OPENAI_MODEL"),
    instructions= instructions,
    input=prompt,
    text_format = ResumeAnalysis
)
 
result = response.output_parsed
print(result)
print("---------------------------------------")
print(result.name)
print(result.skills)
 