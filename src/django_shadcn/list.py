import typer
from rich import box
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text

from .components import registry
from .console import console
from .constants import destination_for

app = typer.Typer(no_args_is_help=True)


def get_all_components() -> list[str]:
    """Fetch all available components"""
    return list(registry.keys())


def is_installed(component: str) -> bool:
    """Whether the component already has files in the current project."""
    return destination_for(component).is_dir()


@app.command(name='list')
def list_components():
    """List all available components"""
    components = get_all_components()
    installed = {name for name in components if is_installed(name)}

    styled_components = [
        Text(
            f'{component} *' if component in installed else component,
            style='bold green' if component in installed else 'green',
        )
        for component in sorted(components)
    ]

    columns = Columns(styled_components, column_first=False, padding=(0, 2))

    subtitle = f'[bold cyan]Total: {len(components)} components'
    if installed:
        subtitle += f' | {len(installed)} installed (*)'

    panel = Panel(
        columns,
        title='[bold blue]Available Components',
        subtitle=subtitle,
        box=box.ROUNDED,
        border_style='blue',
        padding=(1, 2),
    )

    console.print(panel)
