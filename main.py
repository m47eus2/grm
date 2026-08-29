import typer
import subprocess

app = typer.Typer()

@app.command()
def create():
    try:
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "branch", "-m", "main"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{e.cmd}")

@app.command()
def clone(repoUrl: str):
    subprocess.run(["git", "clone", repoUrl])

@app.command()
def status(verbose: bool = False):
    if verbose:
        subprocess.run(["git", "status"])
    else:
        subprocess.run(["git", "status", "--branch", "--short"])

@app.command()
def stage(fileName: str = "", all: bool = False):
    if all:
        subprocess.run(["git", "add", "."])
    else:
        subprocess.run(["git", "add", fileName])

@app.command()
def commit(title: str, desc: str = ""):
    if len(desc) > 0:
        subprocess.run(["git", "commit", "-m", title, "-m", desc])
    else:
        subprocess.run(["git", "commit", "-m", title])

@app.command()
def history(verbose: bool = False):
    if verbose:
        subprocess.run(["git", "log", "--graph"])
    else:
        subprocess.run(["git", "log", "--oneline", "--graph"])

if __name__ == "__main__":
    app()