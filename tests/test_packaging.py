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
CI_WORKFLOW = REPO_ROOT / '.github' / 'workflows' / 'ci.yml'
README = REPO_ROOT / 'README.md'


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


def python_versions_in_ci() -> list[str]:
    matrix = re.search(
        r'python-version:\s*\[(.*?)\]',
        CI_WORKFLOW.read_text(encoding='utf-8'),
    )
    return re.findall(r'\d+\.\d+', matrix.group(1))


def python_versions_in_the_readme() -> list[str]:
    badge = re.search(
        r'img\.shields\.io/badge/python-([^-]+)-',
        README.read_text(encoding='utf-8'),
    )
    return re.findall(r'\d+\.\d+', badge.group(1))


def test_the_readme_badge_names_the_versions_ci_tests():
    """Unlike the others, this badge is typed in rather than queried.

    shields.io's `badge/` endpoint renders whatever text it is given, so
    nothing but this stops the README claiming a version the suite has
    never run on.
    """
    tested = python_versions_in_ci()

    assert tested, 'the CI matrix was not found; this test guards nothing'
    assert python_versions_in_the_readme() == tested


def test_the_declared_minimum_is_the_oldest_version_tested():
    config = tomllib.loads(
        (REPO_ROOT / 'pyproject.toml').read_text(encoding='utf-8')
    )
    oldest = min(
        python_versions_in_ci(), key=lambda v: tuple(map(int, v.split('.')))
    )

    assert config['project']['requires-python'] == f'>={oldest}'
