import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("ValueError: Api Error")


client = Groq(api_key=my_api_key)

role = "user"
model = "openai/gpt-oss-120b"
prompt = "Explain Python dictionaries with an example"

system_message = {"role": "system", "content": "Beginner-Friendly Python Tutor."}

message = {"role": role, "content": prompt}

messages = [system_message, message]

response = client.chat.completions.create(
    model=model, messages=messages, temperature=1.5
)

print(response.choices[0].message.content.strip())

print(
    f"Input Token used-->{response.usage.prompt_tokens} Response Token used-->{response.usage.completion_tokens} Total Token used-->{response.usage.prompt_tokens + response.usage.completion_tokens} "
)
