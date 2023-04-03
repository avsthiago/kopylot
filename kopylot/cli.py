import subprocess
from typing import List

import rich
import typer
from InquirerPy import inquirer
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text

from kopylot.audit import create_printtable_table, run_audit
from kopylot.chat import run_chat
from kopylot.diagnose import run_diagnose
from kopylot.llm import validate_token
from kopylot.utils import ai_print
from kopylot.version import __version__

app = typer.Typer(no_args_is_help=True)
console = Console()


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
    resource_type: str = typer.Argument(..., help="The type of resource to diagnose. E.g.: pod, deployment, service"),
    resource_name: str = typer.Argument(..., help="The name of the resource to diagnose"),
    show_describe: bool = typer.Option(False, "--show-describe", help="Show the output of `kubectl describe`"),
    no_color: bool = typer.Option(False, "--no-color", help="Disable color output and borders"),
) -> str:
    """
    Diagnose a resource e.g. pod, deployment, or service using an LLM model.
    """
    # run `kubectl describe` for the resource
    describe_command = f"kubectl describe {resource_type} {resource_name}"

    with console.status("[bold green]Getting resource description..."):
        describe_result = subprocess.run(describe_command, shell=True, capture_output=True)

    describe_decoded_result = describe_result.stdout.decode("utf-8")
    if show_describe:
        if no_color:
            print(describe_decoded_result)
        else:
            rich.print(Panel(Text(describe_decoded_result), title=f"{resource_type.title()} description"))

    with console.status("[bold green]Running diagnosis..."):
        diagnose_result: str = run_diagnose(resource_type, describe_decoded_result)
    print("\n")
    ai_print(f"Diagnosis for the {resource_type.title()} {resource_name}", diagnose_result, no_color)
    print("\n")

    return diagnose_result


@app.command()
def audit(
    resource_type: str = typer.Argument(..., help="The type of resource to audit. E.g: pod, deployment, service"),
    resource_name: str = typer.Argument(..., help="The name of the resource to audit"),
    no_color: bool = typer.Option(False, "--no-color", help="Disable color output and borders"),
) -> str:
    """
    Audit a pod, deployment, or service using an LLM model.
    """
    # run `kubectl get {resource_type} {resource_name} -oyaml` to get the resource's yaml
    get_yaml_command = f"kubectl get {resource_type} {resource_name} -oyaml"

    with console.status("[bold green]Getting resource yaml..."):
        get_yaml_restult = subprocess.run(get_yaml_command, shell=True, capture_output=True)

    get_yaml_result_decoded = get_yaml_restult.stdout.decode("utf-8")

    with console.status("[bold green]Running audit..."):
        audit_result: str = run_audit(resource_type, get_yaml_result_decoded)
    print("\n")
    table_title = f"\U0001f916 Audit for the {resource_type.title()} {resource_name}"
    console.print(create_printtable_table(audit_result, table_title, no_color))
    print("\n")

    return audit_result


@app.command()
def chat() -> None:
    """
    Start a chat with kopylot to generate kubectl commands based your inputs.
    """
    while True:
        user_prompt = inquirer.text(
            message="\nAsk me something:", qmark="", amark="", long_instruction="\u2139\ufe0f  Empty to quit."
        ).execute()
        if user_prompt == "":
            break

        with console.status("[bold green]Generting kubectl command..."):
            command = run_chat(user_prompt)

        rich.print(
            Panel(
                Syntax(command, "bash", theme="native"),
                title="\U0001f916 Your kubectl command",
                title_align="center",
                border_style="green",
                expand=False,
            )
        )
        print("\n")

        confirmation = inquirer.confirm(message="Run the command?", qmark="", amark="", default=True).execute()
        if confirmation:
            subprocess.run(command, shell=True)


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"KoPylot version: {__version__}")
        raise typer.Exit()


@app.callback()
def common(
    ctx: typer.Context,
    version: bool = typer.Option(None, "--version", callback=version_callback),
) -> None:
    pass


def main() -> None:
    if validate_token():
        app()
    else:
        import sys

        rich.print("[bold red]Error:[/bold red] KOPYLOT_AUTH_TOKEN not set.")
        sys.exit(1)


if __name__ == "__main__":
    main()
