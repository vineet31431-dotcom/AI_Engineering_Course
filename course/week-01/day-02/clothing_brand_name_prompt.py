import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API error")

# Register as client
client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"
prompt = input("Ask Anything: ")

message_system={
    "role": "system",
    "content":"""You are a Clothing brand expert. your job is to provide me with the best name for my clothing brand.
    You will provide me with 5 unique names for my clothing brand. You will not provide any other information except the names of the clothing brand."""
}
# Key value pair message and content
message = {
    "role": role,
    "content": prompt
}

# list of messages
messages = [message_system,message]

response = client.chat.completions.create(model=model, messages=messages,temperature=2)

# Print clean text response from openai/gpt-oss-120b

# print(response.choices[0].message.content)
print(response.choices[0].message.content.strip())
