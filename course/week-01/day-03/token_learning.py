import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Value Error: API error")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"

role = "user"
# multiple prompts
prompt1 = "Hi"
prompt2 = "Explain JSON in detail in 50 words"
prompt3 = "Write an essay on machine learning under 250 words"

# list of prompts
prompts = [prompt1, prompt2, prompt3]

# Set Assistant role(System role)

message_system = {"role": "system", "content": "Friendly Assistant"}


for prompt in prompts:
    # Key value pair message and content(User side)
    message = {"role": role, "content": prompt}

    messages = [message_system, message]

    # Max token usage is set to 100
    response = client.chat.completions.create(
        model=model, messages=messages, max_tokens=100
    )

    usage = response.usage
    print(
        f"Prompt: {prompt} --> your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total_tokens: {usage.prompt_tokens + usage.completion_tokens} Finish reason: {response.choices[0].finish_reason}"
    )
