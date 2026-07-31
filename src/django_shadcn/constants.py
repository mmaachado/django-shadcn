from pathlib import Path

COMPONENTS_REPO_URL = 'gh:mmaachado/django-shadcn'
COMPONENTS_REPO_REF = 'master'

TEMPLATES_DIRECTORY = Path('templates')
DEFAULT_COMPONENTS_DIRECTORY = TEMPLATES_DIRECTORY / 'cotton'

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

    return DEFAULT_COMPONENTS_DIRECTORY / component
