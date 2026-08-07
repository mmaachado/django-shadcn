"""Locating the component templates that ship with the package."""

from pathlib import Path

_BUNDLED = Path(__file__).parent / '_components'
_CHECKOUT = Path(__file__).parents[2] / 'components'


def components_root() -> Path:
    """The directory holding one subdirectory per component.

    The wheel carries the templates under `_components`. Running from a
    source checkout there is no such directory, because the build is what
    puts it there, so fall back to the tree the build copies from.
    """
    if _BUNDLED.is_dir():
        return _BUNDLED

    if _CHECKOUT.is_dir():
        return _CHECKOUT

    raise RuntimeError(
        'the component templates are missing from this installation'
    )


def source_for(component: str) -> Path:
    """Where a component's files are read from."""
    return components_root() / component
