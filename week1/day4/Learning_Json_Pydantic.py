import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel


load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("ValueError: API Error")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"

#Create a pydantic model to validate the output from the model
class Ticket(BaseModel):
    name: str
    email: str
    issue: str
    phone_no: str

#Generate JSON schema from pydantic model to use in system prompt for validation
schema = Ticket.model_json_schema()

#Setting the response format to json_object to get a valid JSON output from the model
response_format ={
    "type":"json_object"
}

#System prompt:-
system_prompt = f"""
 Extract the personal information from the ticket strictly based on this schema and give a json output: {schema}
 Guidelines for the 'issue' field:
- Keep it extremely brief and concise (under 4-5 words).
- Summarize only the core problem (e.g., "iphone not working").
- Exclude unnecessary context like where or when they bought it.
 """

system_message = {
     "role":"system",
     "content": system_prompt
 }

#Customer ticket text to extact personal details
text = """Hi My name is vineet. I am from delhi and yesterday i bought an iphone from your store and now
its not working please contact me my email address is abc@gmail my phone number is 97564.
regards
vineet
"""

#User prompt to extract personal details from the customer ticket text
prompt = f"""
This is a customer ticket.Extract personal details from this.{text}
"""

#Setting user message with role and content
message = {
    "role": role,
    "content": prompt
}

#Passing system and user messages to the model
messages = [system_message,message]

#Generating response from the model with the specified response format and setting temperature to 0 for fixed and predictable output
response = client.chat.completions.create(model=model,messages=messages,response_format=response_format,temperature=0)

#Extracting the raw JSON output from the model response and printing it
answer = response.choices[0].message.content
print("Raw JSON output:" + answer)
print("-" * 50)

#Using pydantic built-in JSON validator directly to validate the output and create a Ticket object
ticket = Ticket.model_validate_json(answer)

#Printing extracted personal details from the ticket
print(ticket.name)
print(ticket.email)
print(ticket.phone_no)
print(ticket.issue)