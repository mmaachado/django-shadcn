from importlib.metadata import PackageNotFoundError, version
from typing import Annotated

import typer

from .add import app as add_app
from .console import console
from .initialize import app as init_app
from .list import app as list_app

app = typer.Typer(no_args_is_help=True, add_completion=False)


def _show_version(requested: bool) -> None:
    if not requested:
        return

    try:
        console.print(version('django-shadcn'))
    except PackageNotFoundError:
        console.print('unknown')

    raise typer.Exit()


@app.callback()
def callback(
    show_version: Annotated[
        bool,
        typer.Option(
            '--version',
            '-V',
            callback=_show_version,
            is_eager=True,
            help='Show the installed version and exit',
        ),
    ] = False,
):
    """
    shadcn/ui for your Django projects
    """


app.add_typer(init_app)
app.add_typer(add_app)
app.add_typer(list_app)
