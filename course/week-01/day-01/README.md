# Day 1 — First Groq Request

## What I am learning

- Make a Groq client with an API key.
- Send a prompt to a model.
- Print the model's reply.

## Concepts

The script asks me for a prompt, sends it to Groq, and prints the reply. It uses `python-dotenv` to read settings from the environment or a local `.env` file.

## File

- [`hello_llm.py`](hello_llm.py) — sends one prompt and prints one reply.
- [`.python-version`](.python-version) — selects Python 3.11.

## Run

Set `GROQ_API_KEY` in your environment. From this folder, run:

```powershell
uv run --with groq --with python-dotenv python hello_llm.py
```

This folder does not have a `pyproject.toml`. The command supplies the packages the script imports. You also need internet access and a valid Groq key.

## Exercise

Try a few prompts and compare the replies. This script does not save earlier messages, so each run is a new chat.