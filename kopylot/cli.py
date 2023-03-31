import subprocess
from typing import List

import rich
import typer
from rich.panel import Panel
from rich.text import Text

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
    show_describe: bool = typer.Option(False, "--show-describe", help="Show the output of `kubectl describe`"),
    no_color: bool = typer.Option(False, "--no-color", help="Disable color output and borders"),
) -> str:
    """
    Diagnose a pod, deployment, or service using a LLM model.
    """
    # run `kubectl describe` for the resource
    describe_command = f"kubectl describe {resource_type} {resource_name}"
    describe_result = subprocess.run(describe_command, shell=True, capture_output=True)
    describe_decoded_result = describe_result.stdout.decode("utf-8")
    if show_describe:
        if no_color:
            print(describe_decoded_result)
        else:
            rich.print(Panel(Text(describe_decoded_result), title=f"{resource_type.title()} description"))

    diagnose_result: str = run_diagnose(resource_type, describe_result.stdout.decode("utf-8"))

    if no_color:
        print(f"\nDiagnosis for the {resource_type.title()} {resource_name}:\n{diagnose_result}")
        return diagnose_result

    rich.print(
        Panel(
            Text(diagnose_result),
            title=f"\U0001f916 Diagnosis for the {resource_type.title()} {resource_name}",
            style="bold green",
        )
    )
    return diagnose_result


if __name__ == "__main__":
    app()
