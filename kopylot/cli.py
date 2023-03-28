import typer

app = typer.Typer()


@app.command()
def kubectl(
    command: str = typer.Argument(..., help="The kubectl command to run."),
    kubeconfig: str = typer.Option(None, help="Path to the kubeconfig file."),
    context: str = typer.Option(None, help="The name of the kubeconfig context to use."),
    namespace: str = typer.Option(None, help="The namespace to use for the command."),
    output: str = typer.Option(None, help="Output format."),
    watch: bool = typer.Option(False, help="Watch for changes."),
    timeout: int = typer.Option(None, help="The number of seconds to wait for the command to complete."),
) -> None:
    """
    Run a kubectl command with the specified options.
    """
    # Call kubectl command with specified options
    kubectl_command = f"kubectl {command}"
    if kubeconfig:
        kubectl_command += f" --kubeconfig={kubeconfig}"
    if context:
        kubectl_command += f" --context={context}"
    if namespace:
        kubectl_command += f" --namespace={namespace}"
    if output:
        kubectl_command += f" -o {output}"
    if watch:
        kubectl_command += " --watch"
    if timeout:
        kubectl_command += f" --timeout={timeout}"

    # Print the kubectl command that would be run
    typer.echo(f"Running command: {kubectl_command}")
    # Run the kubectl command in the terminal using sysprocess
    import subprocess

    subprocess.run(kubectl_command, shell=True)


if __name__ == "__main__":
    app()
