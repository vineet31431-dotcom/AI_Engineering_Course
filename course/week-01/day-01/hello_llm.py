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

# Key value pair message and content (Perfectly fixed!)
message = {
    "role": role,
    "content": prompt
}

# list of messages (Perfectly fixed!)
messages = [message]

response = client.chat.completions.create(model=model, messages=messages)

# Print just the clean text response from Llama 3.3
# print(response.choices[0].message.content)
print(response.choices[0].message.content.strip())
