import os
import re

import openai

from . import prompts

openai.api_key = os.getenv("OPENAI_API_KEY", "")

# Regular expression pattern to match common errors in pod descriptions
error_pattern = re.compile(r"\b(unsupported|invalid|missing|failed|error)\b", re.IGNORECASE)


def run_diagnose(resource_type: str, describe_result: str) -> str:
    prompt = prompts.diagnose_prompt(resource_type, describe_result)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
    )

    solution: str = response.choices[0].text.strip()
    if error_pattern.search(solution):
        return solution
    else:
        return "No errors detected"
