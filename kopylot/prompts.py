def diagnose_prompt(resource_type: str, resource_description: str) -> str:
    prompt = (
        "I want you to act as a professional Kubernetes administrator. You will receive the description of a "
        f"{resource_type} resource and will investigate if there are any issues. Provide advice if there are issues. "
        "If there are no problems, say 'No errors detected'.\n"
        "List the possible problems in bullet points. Write the solutions in imperative tense, e.g., "
        "'Restart the pod' or 'Increase the memory limit'. Provide just a few bullet points.\n\n"
        f"{resource_type.upper()} DESCRIPTION:\n"
        f"```\n{resource_description}\n```\n"
        "THE SOLUTION:\n"
    )
    return prompt


def audit_prompt(resource_type: str, resource_yaml: str) -> str:
    return (
        f"You are a Kubernetes expert searching for vulnerabilities in a {resource_type} yaml. Scan the following"
        f" {resource_type} definition and list the vulnerabilities found. You should return the result as a json"
        " containing two columns (vulnerability, severity). The column vulnerability should contain a long text.The"
        " allowed severities are LOW, MEDIUM, HIGH, CRITICAL. don't write anything else besides the"
        f" json\n\n{resource_yaml}\n\nJSON:\n"
    )
