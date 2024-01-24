import os
import sys

import openai
import rich

openai.api_key = os.getenv("KOPYLOT_AUTH_TOKEN", "")


def validate_token() -> None:
    if openai.api_key == "":
        rich.print(
            "[bold red]Error:[/bold red] Please set your OpenAI API key as an environment variable named"
            " KOPYLOT_AUTH_TOKEN"
        )
        sys.exit(1)


def ask_llm(prompt: str, temperature: float = 0.7, max_tokens: int = 2048) -> str:
    validate_token()
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return str(response.choices[0].text.strip())
