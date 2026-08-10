"""The registry in components.py must match what is on disk.

A component missing from the registry cannot be installed, and a registry
entry without a directory makes `add` copy nothing while reporting success.
"""

import re
from pathlib import Path

import pytest

from django_shadcn.components import registry

# Cotton tags that never map to a component of their own. `component` is the
# dynamic tag: <c-component :is="..."> resolves at render time.
RESERVED_TAGS = frozenset({'vars', 'slot', 'component'})

COTTON_TAG = re.compile(r'<c-([a-zA-Z0-9_]+)')

# Alpine directives that a plugin registers, mapped to the package shipping
# it. Anything Alpine's core provides has no entry here.
PLUGIN_DIRECTIVES = {'x-collapse': '@alpinejs/collapse'}


def components_used_by(directory: Path) -> set[str]:
    """Root component names referenced from within a component."""
    used: set[str] = set()
    for template in directory.rglob('*.html'):
        used.update(COTTON_TAG.findall(template.read_text(encoding='utf-8')))
    return used - RESERVED_TAGS - {directory.name}


def test_every_directory_has_a_registry_entry(component_names):
    missing = set(component_names) - set(registry)
    assert not missing, f'components without a registry entry: {missing}'


def test_every_registry_entry_has_a_directory(component_names):
    missing = set(registry) - set(component_names)
    assert not missing, f'registry entries without a directory: {missing}'


def test_declared_dependencies_are_known_components(component_names):
    for component, entry in registry.items():
        unknown = set(entry.depends) - set(component_names)
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
        undeclared = used - set(registry[component].depends)
        assert not undeclared, (
            f'{component} uses undeclared components: {sorted(undeclared)}'
        )


def test_no_duplicate_dependencies():
    for component, entry in registry.items():
        assert len(entry.depends) == len(set(entry.depends)), (
            f'{component} declares a duplicate dependency'
        )


def plugins_used_by(directory: Path) -> set[str]:
    """Packages the markup in a component needs Alpine to have loaded."""
    markup = '\n'.join(
        template.read_text(encoding='utf-8')
        for template in directory.rglob('*.html')
    )
    return {
        package
        for directive, package in PLUGIN_DIRECTIVES.items()
        if directive in markup
    }


def test_plugin_directives_match_the_declared_scripts(
    component_names, components_root
):
    """Nothing else catches this one.

    An undeclared component dependency leaves a visible hole in the page.
    A missing Alpine plugin renders perfectly and silently does nothing, so
    the registry is the only place the requirement can live.
    """
    known = set(PLUGIN_DIRECTIVES.values())

    for component in component_names:
        used = plugins_used_by(components_root / component)
        declared = set(registry[component].scripts)

        assert used <= declared, (
            f'{component} uses {sorted(used - declared)} without declaring it'
        )
        assert (declared & known) <= used, (
            f'{component} declares {sorted(declared - used)}, unused by its '
            'markup'
        )


def owning_tag(source: str, index: int) -> str:
    """The tag whose attribute list contains the character at `index`."""
    start = source.rfind('<', 0, index)
    return source[start : start + 3]


def test_attrs_are_never_spread_onto_another_component(components_root):
    """cotton silently drops {{ attrs }} placed on a <c-*> tag.

    Its compiler masks {{ ... }} before parsing the tag, so the attributes
    never reach the child and disappear without an error. Components that
    build on another one have to render the HTML element themselves.
    """
    offenders = []

    for template in components_root.rglob('*.html'):
        source = template.read_text(encoding='utf-8')
        for match in re.finditer(r'\{\{\s*attrs\s*\}\}', source):
            if owning_tag(source, match.start()) == '<c-':
                offenders.append(template.relative_to(components_root))

    assert not offenders, f'attrs spread onto a component in: {offenders}'


def test_every_component_has_an_index_template(
    component_names, components_root
):
    """<c-name> resolves to name/index.html, so it has to exist.

    `allauth` ships page templates into templates/account/ rather than a
    cotton component. `form` and `typography` are only sets of
    subcomponents, with no root element of their own.
    """
    without_root = {'allauth', 'form', 'typography'}

    for component in set(component_names) - without_root:
        index = components_root / component / 'index.html'
        assert index.is_file(), f'{component} has no index.html'


def test_install_commands_in_the_docs_name_real_components():
    """The docs shipped an `add toggle-group` that the CLI rejected."""
    docs = Path(__file__).resolve().parent.parent / 'docs' / 'content'

    if not docs.is_dir():
        pytest.skip('docs/ is a separate repository and is not checked out')

    commands = re.compile(r'django_shadcn@latest add ([a-z0-9_\- ]+)')
    wrong = []

    for page in sorted(docs.glob('*.md')):
        for line in commands.findall(page.read_text(encoding='utf-8')):
            for name in line.split():
                if name not in registry:
                    wrong.append(f'{page.name}: add {name}')

    assert not wrong, f'install commands that fail: {wrong}'
