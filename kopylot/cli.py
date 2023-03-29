import subprocess
from typing import List

import typer

from .diagnose import run_diagnose

app = typer.Typer()


@app.command()
def ctl(args: List[str]) -> subprocess.CompletedProcess:
    """
    A wrapper around kubectl. The arguments passed to the ctl subcommand are interpreted by kubectl.
    """
    kubectl_args = " ".join(args)
    kubectl_command = f"kubectl {kubectl_args}"
    return subprocess.run(kubectl_command, shell=True)


@app.command()
def diagnose(
    resource_type: str = typer.Argument(
        ..., help="The type of resource to diagnose. Must be one of: pod, deployment, service"
    ),
    resource_name: str = typer.Argument(..., help="The name of the resource to diagnose"),
) -> str:
    """
    Diagnose a pod, deployment, or service using a LLM model.
    """
    # run kubectl describe for the resource
    describe_command = f"kubectl describe {resource_type} {resource_name}"
    describe_result = subprocess.run(describe_command, shell=True, capture_output=True)
    print(describe_result)

    diagnose_result = run_diagnose(resource_type, describe_result.stdout.decode("utf-8"))
    print(diagnose_result)
    return diagnose_result


if __name__ == "__main__":
    app()
