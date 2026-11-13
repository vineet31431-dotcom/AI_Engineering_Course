# Day 2 — Prompts and Token Counts

## What I am learning

- Use a system message to guide a reply.
- Send a fixed prompt or ask for one in the terminal.
- Read token counts from the response.

## Concepts

`practice.py` asks a fixed question about Python dictionaries. It prints the prompt, reply, and token counts.

`clothing_brand_name_prompt.py` asks me for a prompt and requests five clothing brand names. The model's reply is not checked to make sure it gives five names.

## Files

- [`practice.py`](practice.py) — fixed Python question and token counts.
- [`clothing_brand_name_prompt.py`](clothing_brand_name_prompt.py) — interactive brand-name prompt.
- [`__init__.py`](__init__.py) — prints a greeting when its `main()` function is called. It is not used by these exercises.
- [`.python-version`](.python-version) — selects Python 3.11.

## Run

Set `GROQ_API_KEY` in your environment. From this folder, run either script:

```powershell
uv run --with groq --with python-dotenv python practice.py
uv run --with groq --with python-dotenv python clothing_brand_name_prompt.py
```

This folder does not have a `pyproject.toml`. These commands supply the packages the scripts import. You need internet access and a valid Groq key.

## Exercise

Change the prompt and compare the replies. In `practice.py`, look at the prompt, completion, and total token counts.