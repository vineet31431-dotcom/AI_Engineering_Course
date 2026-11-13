# AI Resume Analyzer

I started this project to learn how to read a resume, ask an AI model to find details, and compare skills with a job.

The project is still a prototype. The code is in one file, and the current run does not finish analyzing a resume.

## What the code has

- Pydantic models for candidate details, job requirements, and skill-match results. Pydantic checks that data has the fields and types the model expects.
- Code that builds a JSON schema and sends a request to Groq.
- Helper functions to read text from PDF and DOCX files.
- Code that compares candidate skills with required skills and calculates a match percentage. It treats upper- and lowercase letters as the same.

These parts are not connected in a full working flow yet. The active code tries to open `dummy_resume_for_pypdf.pdf`, but that file is not here. The included samples are [`dummy_resume.pdf`](dummy_resume.pdf) and [`dummy_resume.docx`](dummy_resume.docx). The code has parsing helpers for both formats, but the active path does not call them.

## Tools used

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/) to install the packages
- Groq to send requests to an AI model
- Pydantic to check data
- pypdf and python-docx to read PDF and DOCX files
- python-dotenv to load settings from `.env`
- email-validator for the Pydantic email field

## Setup

You need Python 3.11 or newer, uv, and a Groq API key.

From the repository root, go to the project folder:

```powershell
Set-Location 'projects\AI-Resume-Analyzer'
```

If you do not already have a `.env` file, copy the example:

```powershell
if (-not (Test-Path .env)) { Copy-Item .env.example .env }
```

Put your key in `.env` as the value for `GROQ_API_KEY`. Keep `.env` private and do not commit it. The `.env.example` file has only a placeholder.

Install the packages listed in the project files:

```powershell
uv sync
```

## Run

From the project folder, run:

```powershell
uv run python main.py
```

The script needs your API key. It then tries to open the missing `dummy_resume_for_pypdf.pdf` and prints a file error. It does not use either included sample file in this run.

## What still needs work

- The script has no command-line option to choose a resume.
- The PDF and DOCX helpers are not connected to the active model request.
- The file path used by the active code is missing.
- The job model has experience fields, but the matching code only compares skills.
- There are no automated tests.
- The model request needs a valid Groq key and an internet connection.

## Ideas for later

These are not built yet:

- Connect the PDF and DOCX helpers to the model request.
- Let me choose a resume and job requirements when I run the program.
- Split the code into smaller files.
- Add tests that do not call the live model.

See the [projects list](../README.md) or go back to the [repository home](../../README.md).