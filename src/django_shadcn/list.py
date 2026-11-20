import typer
from rich import box
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text

from .bundle import source_for
from .components import registry
from .console import console
from .constants import destination_for

app = typer.Typer(no_args_is_help=True)


def get_all_components() -> list[str]:
    """Fetch all available components"""
    return list(registry.keys())


def is_installed(component: str) -> bool:
    """Whether the project holds every file this component ships.

    Neither the destination existing nor one matching file is enough:
    `allauth` writes into templates/account/ under django-allauth's own
    template names, so a project that hand-wrote login.html matches any
    looser test. Demanding the whole set biases the answer towards a false
    negative, and that is the cheap direction — it costs a redundant `add`,
    which in safe mode changes nothing, where a false positive costs the
    install the user never makes.
    """
    destination = destination_for(component)
    source = source_for(component)
    shipped = [path for path in source.rglob('*') if path.is_file()]

    return bool(shipped) and all(
        (destination / path.relative_to(source)).is_file() for path in shipped
    )


def _panel(title: str, names: list[str], installed: set[str]) -> Panel:
    styled = [
        Text(
            f'{name} *' if name in installed else name,
            style='bold green' if name in installed else 'green',
        )
        for name in sorted(names)
    ]

    subtitle = f'[bold cyan]Total: {len(names)}'
    mine = installed & set(names)
    if mine:
        subtitle += f' | {len(mine)} installed (*)'

    return Panel(
        Columns(styled, column_first=False, padding=(0, 2)),
        title=f'[bold blue]{title}',
        subtitle=subtitle,
        box=box.ROUNDED,
        border_style='blue',
        padding=(1, 2),
    )


@app.command(name='list')
def list_components():
    """List all available components and blocks"""
    names = get_all_components()
    installed = {name for name in names if is_installed(name)}
    blocks = [name for name in names if registry[name].block]
    components = [name for name in names if not registry[name].block]

    console.print(_panel('Available Components', components, installed))
    console.print(_panel('Blocks', blocks, installed))
