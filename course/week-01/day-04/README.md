# Day 4 — JSON and Pydantic

## What I am learning

- Make a Pydantic model to describe the fields I need.
- Make a JSON schema from that model.
- Check JSON returned by a model.

## Concepts

`learning_json_pydantic.py` defines a `Ticket` with name, email, issue, and phone fields. It sends a sample customer message to Groq and asks for a JSON reply. Pydantic then checks that the reply can be read as a `Ticket`.

## Files

- [`learning_json_pydantic.py`](learning_json_pydantic.py) — sends the ticket prompt and checks the JSON reply.
- [`pyproject.toml`](pyproject.toml) and [`uv.lock`](uv.lock) — list this folder's packages and uv settings.
- [`src/day4/__init__.py`](src/day4/__init__.py) — has a `main()` function that prints a greeting. It is separate from the exercise.
- [`.python-version`](.python-version) — selects Python 3.11.

## Run

The script needs its listed packages, `GROQ_API_KEY`, and internet access.

The `pyproject.toml` lists a `mini-project` workspace folder that is not in this day folder. The portfolio project is in a different location. Because of this, I have not confirmed that `uv sync` works here.

When the required packages are available, run this from the day folder:

```powershell
python learning_json_pydantic.py
```

## Exercise

Run the script and look at the JSON reply and the printed ticket fields. The example message is written in the script; it does not ask for a ticket in the terminal.