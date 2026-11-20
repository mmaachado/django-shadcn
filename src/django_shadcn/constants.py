from pathlib import Path

from .components import registry

TEMPLATES_DIRECTORY = Path('templates')
DEFAULT_COMPONENTS_DIRECTORY = TEMPLATES_DIRECTORY / 'cotton'

# One directory per block, so syncing a block mirrors its own pages and
# cannot reach the pages of another.
BLOCKS_DIRECTORY = TEMPLATES_DIRECTORY / 'blocks'

# Components that install to templates/ root instead of templates/cotton/,
# mapped to their destination folder name
TEMPLATE_ROOT_COMPONENTS = {
    'allauth': 'account',  # allauth component installs to templates/account/
}


def destination_for(component: str) -> Path:
    """Where a component's files belong inside the project."""
    root_folder = TEMPLATE_ROOT_COMPONENTS.get(component)

    if root_folder:
        return TEMPLATES_DIRECTORY / root_folder

    if component in registry and registry[component].block:
        return BLOCKS_DIRECTORY / component

    return DEFAULT_COMPONENTS_DIRECTORY / component
