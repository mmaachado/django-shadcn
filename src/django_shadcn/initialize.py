import shutil
from pathlib import Path

import typer
from rich.panel import Panel

from .bundle import components_root
from .console import console
from .constants import DEFAULT_COMPONENTS_DIRECTORY

app = typer.Typer(no_args_is_help=True, add_completion=False)

THEME_FILE = 'input.css'


@app.command(name='init')
def init():
    """
    Initialize setup for django_shadcn components
    """
    DEFAULT_COMPONENTS_DIRECTORY.mkdir(parents=True, exist_ok=True)
    shutil.copy2(components_root() / THEME_FILE, Path.cwd() / THEME_FILE)
    console.print(
        Panel(
            '[bold green]'
            ':rocket: Initialized django_shadcn components!\n\n'
            ':heavy_check_mark: Created '
            + f"'{DEFAULT_COMPONENTS_DIRECTORY}'\n"
            ':heavy_check_mark: Added TailwindCSS config required for '
            'shadcn components\n\n'
            '[/bold green]'
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
