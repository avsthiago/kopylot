def diagnose_prompt(resource_type: str, resource_description: str) -> str:
    return (
        f"Kubernetes {resource_type} description error detection and"
        f" solution\n{resource_type} description:\n{resource_description}\n\nSolution:\n"
    )


def audit_prompt(resource_type: str, resource_yaml: str) -> str:
    return (
        f"You are a Kubernetes experd searching for vulnerabilities on a {resource_type} yaml. Scan the following and"
        " list all the vulnerabilities that you"
        f" encountered\n{resource_type} yaml:\n{resource_yaml}\n\nVulnerabilities:\n"
    )
