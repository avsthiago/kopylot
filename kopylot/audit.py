from kopylot import llm, prompts


def run_audit(resource_type: str, resource_yaml: str) -> str:
    prompt = prompts.audit_prompt(resource_type, resource_yaml)
    return llm.ask_llm(prompt)
