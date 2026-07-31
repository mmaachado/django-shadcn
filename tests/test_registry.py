"""The registry in components.py must match what is on disk.

A component missing from the registry cannot be installed, and a registry
entry without a directory makes `add` copy nothing while reporting success.
"""

import re
from pathlib import Path

from django_shadcn.components import dependencies

# Cotton tags that never map to a component of their own.
RESERVED_TAGS = frozenset({'vars', 'slot'})

COTTON_TAG = re.compile(r'<c-([a-zA-Z0-9_]+)')


def components_used_by(directory: Path) -> set[str]:
    """Root component names referenced from within a component."""
    used: set[str] = set()
    for template in directory.rglob('*.html'):
        used.update(COTTON_TAG.findall(template.read_text(encoding='utf-8')))
    return used - RESERVED_TAGS - {directory.name}


def test_every_directory_has_a_registry_entry(component_names):
    missing = set(component_names) - set(dependencies)
    assert not missing, f'components without a registry entry: {missing}'


def test_every_registry_entry_has_a_directory(component_names):
    missing = set(dependencies) - set(component_names)
    assert not missing, f'registry entries without a directory: {missing}'


def test_declared_dependencies_are_known_components(component_names):
    for component, declared in dependencies.items():
        unknown = set(declared) - set(component_names)
        assert not unknown, f'{component} depends on unknown: {unknown}'


def test_used_components_are_declared_as_dependencies(
    component_names, components_root
):
    """Every <c-other> tag inside a component is a declared dependency.

    Without this, `add` installs a component whose markup references
    another one that never gets copied, and the page renders empty.
    """
    for component in component_names:
        used = components_used_by(components_root / component)
        undeclared = used - set(dependencies[component])
        assert not undeclared, (
            f'{component} uses undeclared components: {sorted(undeclared)}'
        )


def test_no_duplicate_dependencies():
    for component, declared in dependencies.items():
        assert len(declared) == len(set(declared)), (
            f'{component} declares a duplicate dependency'
        )


def test_every_component_has_an_index_template(
    component_names, components_root
):
    """<c-name> resolves to name/index.html, so it has to exist.

    `allauth` ships page templates into templates/account/ rather than a
    cotton component, and `form` is only a set of subcomponents.
    """
    without_root = {'allauth', 'form'}

    for component in set(component_names) - without_root:
        index = components_root / component / 'index.html'
        assert index.is_file(), f'{component} has no index.html'
