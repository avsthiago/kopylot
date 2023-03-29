def diagnose_prompt(resource_type: str, describe_result: str) -> str:
    return (
        f"Kubernetes {resource_type} description error detection and"
        f" solution\n{resource_type} description:\n{describe_result}\n\nSolution:\n"
    )
