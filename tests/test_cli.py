"""CLI smoke tests.

`init` and `add` read the templates that ship with the package, so nothing
here reaches the network.
"""

import runpy
import sys
from importlib.metadata import PackageNotFoundError
from pathlib import Path

import pytest
from typer.testing import CliRunner

from django_shadcn import main
from django_shadcn.add import destination_for, mode_for, resolve_components
from django_shadcn.components import canonical, registry
from django_shadcn.main import app
from django_shadcn.merge import WriteMode

runner = CliRunner()


def test_help_lists_the_commands():
    result = runner.invoke(app, ['--help'])

    assert result.exit_code == 0
    for command in ('init', 'add', 'list'):
        assert command in result.stdout


def test_version_flag():
    result = runner.invoke(app, ['--version'])

    assert result.exit_code == 0
    assert result.stdout.strip()


def test_version_says_unknown_when_the_package_is_not_installed(monkeypatch):
    """Running from a checkout with no install still has to answer."""

    def absent(name):
        raise PackageNotFoundError(name)

    monkeypatch.setattr(main, 'version', absent)

    result = runner.invoke(app, ['--version'])

    assert result.exit_code == 0
    assert 'unknown' in result.stdout


def test_the_module_entry_point_reaches_the_app(monkeypatch):
    """`python -m django_shadcn` is a second door into the same CLI."""
    monkeypatch.setattr(sys, 'argv', ['django_shadcn', '--version'])

    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module('django_shadcn', run_name='__main__')

    assert exit_info.value.code == 0


def test_list_prints_every_component():
    result = runner.invoke(app, ['list'])

    assert result.exit_code == 0
    # Rich wraps the panel into columns, so check names, not layout.
    for component in registry:
        assert component in result.stdout


def test_add_without_arguments_shows_usage():
    result = runner.invoke(app, ['add'])

    # Click writes usage errors to stderr and exits with 2.
    assert result.exit_code == 2
    assert 'Usage' in result.stderr


def test_add_rejects_unknown_components_before_downloading(
    tmp_path, monkeypatch
):
    monkeypatch.chdir(tmp_path)

    result = runner.invoke(app, ['add', 'nope'])

    assert result.exit_code == 1
    assert 'Unknown component' in result.stdout
    assert not list(tmp_path.iterdir()), 'nothing should be written'


def test_every_hyphenated_component_resolves(component_names):
    """<c-toggle-group> is what the user sees, toggle_group is the folder."""
    for name in component_names:
        assert canonical(name.replace('_', '-')) == name


def test_canonical_leaves_an_unknown_name_to_be_rejected():
    assert canonical('does-not-exist') not in registry


@pytest.mark.parametrize(
    'spelling', ['Button', 'BUTTON', ' button ', '\tbutton\n']
)
def test_canonical_tolerates_case_and_surrounding_space(spelling):
    """A shell and a copied doc line both leave these behind."""
    assert canonical(spelling) == 'button'


def test_canonical_normalizes_a_hyphenated_tag_in_any_case():
    assert canonical(' Toggle-Group ') == 'toggle_group'


def test_add_refuses_overwrite_and_sync_together(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    result = runner.invoke(app, ['add', 'button', '--overwrite', '--sync'])

    assert result.exit_code == 1
    assert not list(tmp_path.iterdir())


def test_resolve_pulls_in_dependencies():
    resolved = resolve_components(['combobox'])

    assert resolved == {'combobox', 'button', 'popover', 'icon'}


def test_resolve_handles_several_components():
    resolved = resolve_components(['button', 'card'])

    assert resolved == {'button', 'card'}


def test_resolve_visits_a_shared_dependency_once():
    """dialog and sheet both pull button and icon: the graph is a diamond."""
    resolved = resolve_components(['dialog', 'sheet'])

    assert resolved == {'dialog', 'sheet', 'button', 'icon'}


def test_sync_only_mirrors_what_was_asked_for():
    """Syncing allauth must not wipe customizations in its dependencies."""
    requested = {'allauth'}

    assert mode_for('allauth', requested, WriteMode.sync) is WriteMode.sync
    assert mode_for('button', requested, WriteMode.sync) is WriteMode.safe


def test_other_modes_apply_to_dependencies_too():
    requested = {'allauth'}

    for mode in (WriteMode.safe, WriteMode.overwrite):
        assert mode_for('button', requested, mode) is mode


def test_cotton_components_go_under_the_cotton_directory():
    assert destination_for('button') == Path('templates/cotton/button')


def test_allauth_goes_to_the_templates_root():
    assert destination_for('allauth') == Path('templates/account')
