# AI Engineering Course

I use this repository to keep my course code, notes, and projects as I learn AI Engineering.

## What is here

- [Course](course/README.md): weekly topics and daily exercises.
- [Obsidian notes](notes/obsidian/README.md): the place for my course notes.
- [Projects](projects/README.md): my standalone projects.

```text
course/          Course exercises
notes/obsidian/  Obsidian notes
projects/        Portfolio projects
```

I am currently working through Week 1. The exercises cover Groq prompts, token usage, JSON, and Pydantic. The [AI Resume Analyzer](projects/AI-Resume-Analyzer/README.md) is an early project. Its README explains what the code does and what still needs work.

## Tools

The Python files use Python 3.11 or newer. Some folders have their own `uv` setup, so check the README in the folder you want to run. The exercises and the analyzer use the Groq API. The analyzer also uses Pydantic, pypdf, and python-docx.

## Keep keys private

Do not commit API keys or `.env` files. Use an `.env.example` file as a guide where one is provided. It has a placeholder, not a real key.
