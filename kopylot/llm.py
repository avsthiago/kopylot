import os

import openai

openai.api_key = os.getenv("KOPYLOT_AUTH_TOKEN", "")


def ask_llm(prompt: str, temperature: float = 0.7, max_tokens: int = 2048) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return str(response.choices[0].text.strip())
