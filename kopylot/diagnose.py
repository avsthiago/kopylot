from kopylot import llm, prompts


def run_diagnose(resource_type: str, resource_description: str) -> str:
    prompt = prompts.diagnose_prompt(resource_type, resource_description)
    return llm.ask_llm(prompt)
