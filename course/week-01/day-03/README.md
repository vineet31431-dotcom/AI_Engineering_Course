# Day 3 — Sending Several Prompts

## What I am learning

- Put prompts in a list and send them one at a time.
- Limit the reply length.
- Read token counts and the finish reason from each response.

## Concepts

`token_learning.py` sends three prompts with the same system message. It asks for up to 100 reply tokens and prints the token counts and finish reason.

## Files

- [`token_learning.py`](token_learning.py) — sends the prompts and prints response details.
- [`pyproject.toml`](pyproject.toml) and [`uv.lock`](uv.lock) — list this folder's packages.
- [`src/day3/__init__.py`](src/day3/__init__.py) — has a `main()` function that prints a greeting. It does not run `token_learning.py`.
- [`.python-version`](.python-version) — selects Python 3.11.

## Run

The project lists `python-dotenv`, but the script also imports `groq`. Run it from this folder with Groq added for this command:

```powershell
uv run --with groq python token_learning.py
```

Set `GROQ_API_KEY` in your environment first. You need internet access and a valid Groq key.

## Exercise

Look at the token counts for each prompt. The model may return fewer than 100 tokens.