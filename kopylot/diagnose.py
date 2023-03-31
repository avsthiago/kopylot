import re

from kopylot import llm

from . import prompts

# Regular expression pattern to match common errors in pod descriptions
error_pattern = re.compile(r"\b(unsupported|invalid|missing|failed|error)\b", re.IGNORECASE)


def run_diagnose(resource_type: str, describe_result: str) -> str:
    prompt = prompts.diagnose_prompt(resource_type, describe_result)
    solution = llm.ask_llm(prompt)

    if error_pattern.search(solution):
        return solution
    else:
        return "No errors detected"
