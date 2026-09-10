import typer
from typing import Annotated
import subprocess

app = typer.Typer()

@app.command()
def create(server: Annotated[bool, typer.Option("--server","-s")] = False,):
    """[blue]Create[/blue] a new git repository."""
    if server == 0:
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "branch", "-m", "main"], check=True)
    else:
        subprocess.run(["git", "init", "--bare"], check=True)
        subprocess.run(["git", "branch", "-m", "main"], check=True)


@app.command()
def clone(repoUrl: Annotated[str, typer.Argument()]):
    """[blue]Clone[/blue] a git repository."""
    subprocess.run(["git", "clone", repoUrl])


@app.command()
def status(verbose: Annotated[bool, typer.Option("--verbose", "-v")] = False):
    """Show [blue]status[/blue] of the git repository."""
    if verbose == 0:
        subprocess.run(["git", "status", "--branch", "--short"])
    else:
        subprocess.run(["git", "status"])
        

@app.command()
def stage(
    fileName: Annotated[str, typer.Argument()] = "", 
    all: Annotated[bool, typer.Option("--all", "-a")] = False,
):
    """[blue]Stage[/blue] specified file."""
    if all:
        subprocess.run(["git", "add", "."])
    else:
        subprocess.run(["git", "add", fileName])


@app.command()
def commit(
    title: Annotated[str, typer.Argument()], 
    desc: Annotated[str, typer.Option("--desc", "-d")] = "",
):
    """[blue]Commit[/blue] staged changes."""
    if len(desc) == 0:
        subprocess.run(["git", "commit", "-m", title])
    else:
        subprocess.run(["git", "commit", "-m", title, "-m", desc])


@app.command()
def history(verbose: Annotated[bool, typer.Option("--verbose", "-v")] = False):
    """Shows commits [blue]history[/blue]"""
    if verbose:
        subprocess.run(["git", "log", "--graph"])
    else:
        subprocess.run(["git", "log", "--oneline", "--graph"])


if __name__ == "__main__":
    app()