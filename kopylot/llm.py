import os
import sys

import openai
import rich

openai.api_key = os.getenv("KOPYLOT_AUTH_TOKEN", "")

if not openai.api_key:
    rich.print("[bold red]Error:[/bold red] KOPYLOT_AUTH_TOKEN is not set.")
    sys.exit(1)


def ask_llm(prompt: str, temperature: float = 0.7, max_tokens: int = 2048) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return str(response.choices[0].text.strip())
