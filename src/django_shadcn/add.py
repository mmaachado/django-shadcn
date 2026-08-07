from collections.abc import Iterable
from pathlib import Path
from typing import Annotated

import typer

from .bundle import source_for
from .components import Component, canonical, registry
from .console import console
from .constants import destination_for
from .merge import (
    MergeResult,
    WriteMode,
    conflicting_paths,
    merge,
    obsolete_files,
)

app = typer.Typer(no_args_is_help=True)


def get_component_dependencies(component: str) -> tuple[str, ...]:
    """Fetch dependencies for the given component"""
    return registry.get(component, Component()).depends


def resolve_components(components: Iterable[str]) -> set[str]:
    """The requested components plus everything they depend on."""
    resolved: set[str] = set()
    pending = list(components)

    while pending:
        component = pending.pop()

        if component in resolved:
            continue

        resolved.add(component)
        pending.extend(get_component_dependencies(component))

    return resolved


def _reject_unknown(components: Iterable[str]) -> None:
    """Stop before touching the network or the disk."""
    unknown = sorted(set(components) - set(registry))

    if not unknown:
        return

    console.print(f'[bold red]Unknown component: {", ".join(unknown)}[/]')
    console.print(f'Available: {", ".join(sorted(registry))}')

    raise typer.Exit(code=1)


def _reject_unwritable(components: Iterable[str]) -> None:
    """Stop before the first write, not partway through the run.

    Refusing halfway leaves whatever earlier components already wrote, and
    there is nothing that rolls it back.
    """
    blocked = False

    for component in sorted(components):
        source = source_for(component)

        if not source.is_dir():
            console.print(
                f'[bold red]{component} is missing from this installation[/]'
            )
            blocked = True
            continue

        conflicts = conflicting_paths(source, destination_for(component))

        if not conflicts:
            continue

        console.print(f'[bold red]{component} has paths in the way:[/]')
        for path in conflicts:
            console.print(f'  [red]conflict[/]    {path}')

        blocked = True

    if blocked:
        raise typer.Exit(code=1)


def mode_for(
    component: str, requested: set[str], mode: WriteMode
) -> WriteMode:
    """Mirroring applies only to what was asked for.

    `allauth` pulls in eight components; syncing it must not wipe whatever
    the user changed in `button`.
    """
    if mode is WriteMode.sync and component not in requested:
        return WriteMode.safe

    return mode


def _confirm_removals(component: str, source: Path, destination: Path) -> None:
    doomed = obsolete_files(source, destination)

    if not doomed:
        return

    console.print(
        f'[bold yellow]Syncing {component} removes {len(doomed)} file(s):[/]'
    )
    for path in doomed:
        console.print(f'  [red]- {path}[/]')

    if not typer.confirm('Continue?'):
        raise typer.Abort()


def _report(component: str, result: MergeResult) -> None:
    for path in result.created:
        console.print(f'  [green]created[/]     {path}')
    for path in result.overwritten:
        console.print(f'  [yellow]overwritten[/] {path}')
    for path in result.removed:
        console.print(f'  [red]removed[/]     {path}')
    for path in result.skipped:
        console.print(f'  [dim]skipped     {path}[/]')

    if result.changed:
        console.print(f'[bold green]:heavy_check_mark: Added {component}[/]')
    else:
        console.print(
            f'[dim]:heavy_check_mark: {component} already present[/]'
        )


def _report_scripts(components: Iterable[str]) -> None:
    """Named once for the whole run, however many components asked for it."""
    scripts = sorted(
        {
            script
            for component in components
            for script in registry[component].scripts
        }
    )

    if not scripts:
        return

    console.print(
        f'\n[bold yellow]{", ".join(scripts)}[/] must be loaded before '
        'Alpine, or these components render without behaving.'
    )


@app.command(name='add')
def add(
    components: Annotated[
        list[str], typer.Argument(help='Names of the components to add')
    ],
    overwrite: Annotated[
        bool,
        typer.Option('--overwrite', help='Replace files that already exist'),
    ] = False,
    sync: Annotated[
        bool,
        typer.Option(
            '--sync',
            help='Mirror each component, deleting files it no longer ships',
        ),
    ] = False,
    yes: Annotated[
        bool,
        typer.Option('--yes', '-y', help='Skip the confirmation prompt'),
    ] = False,
):
    """
    Add django_shadcn components to your project

    Existing files are kept untouched unless --overwrite or --sync is given.
    """
    if overwrite and sync:
        console.print(
            '[bold red]Use either --overwrite or --sync, not both[/]'
        )
        raise typer.Exit(code=1)

    components = [canonical(name) for name in components]

    _reject_unknown(components)

    mode = WriteMode.safe
    if overwrite:
        mode = WriteMode.overwrite
    elif sync:
        mode = WriteMode.sync

    requested = set(components)
    to_install = resolve_components(requested)

    _reject_unwritable(to_install)

    skipped = 0

    for component in sorted(to_install):
        source = source_for(component)
        destination = destination_for(component)
        component_mode = mode_for(component, requested, mode)

        if component_mode is WriteMode.sync and not yes:
            _confirm_removals(component, source, destination)

        result = merge(source, destination, component_mode)
        _report(component, result)
        skipped += len(result.skipped)

    if skipped:
        console.print(
            f'\n[yellow]{skipped} existing file(s) left untouched. '
            'Run with --overwrite to replace them.[/]'
        )

    _report_scripts(to_install)
