import subprocess
from typing import List

import typer

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
def diagnose(_: List[str]) -> None:
    """
    Diagnose a pod, deployment, or service using a LLM model.
    """
    pass


if __name__ == "__main__":
    app()
