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


# fmt: off
def kubectl_command_prompt(task_description: str) -> str:
    prompt = (
        "You are a professional Kubernetes administrator. If someone asks you to perform a task, your job is to come up with a kubectl command to interact with the Kubernetes cluster. You can also use bash commands, such as grep, awk, wc, cut, sort, and uniq, to perform the task. "
        "Don't write multiline commands and don't write any explanation.\n\n"
        "You should follow the pattern:\n\n"
        'Task: Show the status of all pods running in the production namespace\n'
        'Command: kubectl get pods -n production\n'
        'Task: give me the cpu and memory utilization of the web-server deployment\n'
        'Command: kubectl top pods -l app=web-server\n'
        'Task: what is the load-balancer service:\n'
        "Command: kubectl get service load-balancer -o jsonpath='{.status.loadBalancer.ingress[0].ip}'\n"
        'Task: List the names of all deployments in the development namespace\n'
        "Command: kubectl get deployments -n development | awk 'NR>1 {print $1}'\n"
        'Task: "Show the names of all pods that are not running"\n'
        'Command: "kubectl get pods | grep -v Running"\n'
        f'Task: "{task_description}"\n'
        "Command:\n"
    )
    return prompt
# fmt: on
