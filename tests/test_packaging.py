"""What the package imports has to be what the package requires.

Pinning the one name this was written for would be worth less than the
line it guards, so this reads the imports instead.
"""

import ast
import re
import sys
import tomllib
from importlib.metadata import packages_distributions
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE = REPO_ROOT / 'src' / 'django_shadcn'


def imported_modules() -> set[str]:
    """Top-level names the package imports from outside itself."""
    modules: set[str] = set()

    for source in PACKAGE.rglob('*.py'):
        tree = ast.parse(source.read_text(encoding='utf-8'))

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                modules.update(
                    alias.name.split('.')[0] for alias in node.names
                )
            # A relative import carries a level; it is our own code.
            elif isinstance(node, ast.ImportFrom) and not node.level:
                modules.add(node.module.split('.')[0])

    return modules - sys.stdlib_module_names - {'django_shadcn'}


def declared_distributions() -> set[str]:
    config = tomllib.loads(
        (REPO_ROOT / 'pyproject.toml').read_text(encoding='utf-8')
    )

    return {
        re.split(r'[<>=!~\[; ]', requirement)[0].lower()
        for requirement in config['project']['dependencies']
    }


def test_every_third_party_import_is_declared():
    """A transitive dependency is a coincidence, not a guarantee.

    rich reached the CLI only because typer happened to bring it. The day
    that stops, every command dies at import time.
    """
    declared = declared_distributions()
    providers = packages_distributions()

    undeclared = sorted(
        module
        for module in imported_modules()
        if not declared.intersection(
            name.lower() for name in providers.get(module, [module])
        )
    )

    assert not undeclared, (
        f'imported by the package, missing from [project.dependencies]: '
        f'{undeclared}'
    )


def test_the_check_can_see_the_imports_it_is_meant_to_guard():
    """A scan that found nothing would pass the test above forever."""
    assert {'rich', 'typer'} <= imported_modules()
