import typer
from rich import print as rprint
from typing_extensions import Annotated
from services import factory
from dotenv import load_dotenv, dotenv_values

load_dotenv

config = dotenv_values(".env")

app = typer.Typer(no_args_is_help=True)

SEPARATOR = "[yellow]==================================[yellow]"


@app.command("info")
def infomethod():
    rprint(SEPARATOR)
    rprint("[yellow]Database backup utility :boom:[yellow]")
    rprint(SEPARATOR)
    rprint("[blue]Use the --help command to see all available options[blue]")


@app.command("backup")
def runbackup():
    try:
        rprint("[blue]Running backup...[blue]")
        rprint(SEPARATOR)
        service = factory.ServiceFactory().create()
        service.backup()
    except KeyError:
        rprint(f"[red]Missing key in config.[red]")


if __name__ == "__main__":
    app()
