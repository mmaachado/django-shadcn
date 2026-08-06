import shutil
from pathlib import Path
from typing import Annotated

import typer
from rich.panel import Panel

from .bundle import components_root
from .console import console
from .constants import DEFAULT_COMPONENTS_DIRECTORY

app = typer.Typer(no_args_is_help=True, add_completion=False)

THEME_FILE = 'input.css'


@app.command(name='init')
def init(
    force: Annotated[
        bool,
        typer.Option('--force', help=f'Replace an existing {THEME_FILE}'),
    ] = False,
):
    """
    Initialize setup for django_shadcn components

    An existing input.css is kept untouched unless --force is given.
    """
    DEFAULT_COMPONENTS_DIRECTORY.mkdir(parents=True, exist_ok=True)

    destination = Path.cwd() / THEME_FILE
    written = force or not destination.exists()

    if written:
        shutil.copy2(components_root() / THEME_FILE, destination)
        theme = (
            ':heavy_check_mark: Added TailwindCSS config required for '
            'shadcn components\n\n'
        )
    else:
        theme = (
            f':heavy_check_mark: Kept your existing {THEME_FILE} '
            '(--force replaces it)\n\n'
        )

    console.print(
        Panel(
            '[bold green]'
            ':rocket: Initialized django_shadcn components!\n\n'
            ':heavy_check_mark: Created '
            + f"'{DEFAULT_COMPONENTS_DIRECTORY}'\n"
            + theme
            + '[/bold green]'
            '[bold yellow]'
            ':bookmark_tabs: Next steps:\n'
            '[/bold yellow]'
            ':arrow_right_hook: Ensure you have tailwind v4 and alpine.js '
            'installed\n'
            ":arrow_right_hook: Add <link rel='stylesheet' "
            "href='{% static 'css/output.css' %}'> to your base HTML "
            'template\n'
            ":arrow_right_hook: Run 'npx @tailwindcss/cli -i input.css "
            "-o static/css/output.css --watch'\n",
            title='Initialization Complete',
            border_style='bold green',
        )
    )
