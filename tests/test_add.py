"""`add`, end to end, from the shipped templates into a project.

`test_merge.py` covers the write modes in isolation; this covers the command
that chooses them, which used to be reachable only over the network.
"""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from django_shadcn import add
from django_shadcn.constants import destination_for
from django_shadcn.main import app

runner = CliRunner()

BUTTON = Path('templates/cotton/button/index.html')


@pytest.fixture
def project(tmp_path: Path, monkeypatch) -> Path:
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_installs_a_component(project):
    result = runner.invoke(app, ['add', 'button'])

    assert result.exit_code == 0
    assert (project / BUTTON).read_text(encoding='utf-8').strip()


def test_installs_dependencies_too(project):
    result = runner.invoke(app, ['add', 'combobox'])

    assert result.exit_code == 0
    for name in ('combobox', 'button', 'popover', 'icon'):
        assert (project / destination_for(name)).is_dir(), name


def test_a_root_component_lands_outside_cotton(project):
    result = runner.invoke(app, ['add', 'allauth'])

    assert result.exit_code == 0
    assert (project / 'templates' / 'account').is_dir()


def test_running_twice_keeps_customizations(project):
    """Issue #22: the default path must never discard user changes."""
    runner.invoke(app, ['add', 'button'])
    (project / BUTTON).write_text('mine', encoding='utf-8')

    result = runner.invoke(app, ['add', 'button'])

    assert result.exit_code == 0
    assert (project / BUTTON).read_text(encoding='utf-8') == 'mine'
    assert 'skipped' in result.stdout
    assert '--overwrite' in result.stdout


def test_overwrite_replaces_but_keeps_extras(project):
    runner.invoke(app, ['add', 'button'])
    (project / BUTTON).write_text('mine', encoding='utf-8')
    extra = project / 'templates' / 'cotton' / 'button' / 'mine.html'
    extra.write_text('mine', encoding='utf-8')

    result = runner.invoke(app, ['add', 'button', '--overwrite'])

    assert result.exit_code == 0
    assert (project / BUTTON).read_text(encoding='utf-8') != 'mine'
    assert extra.is_file(), 'overwrite must not delete unrelated files'


def test_sync_with_yes_removes_what_the_component_no_longer_ships(project):
    runner.invoke(app, ['add', 'button'])
    extra = project / 'templates' / 'cotton' / 'button' / 'mine.html'
    extra.write_text('mine', encoding='utf-8')

    result = runner.invoke(app, ['add', 'button', '--sync', '--yes'])

    assert result.exit_code == 0
    assert not extra.exists()


def test_sync_without_yes_aborts_when_it_cannot_ask(project):
    runner.invoke(app, ['add', 'button'])
    extra = project / 'templates' / 'cotton' / 'button' / 'mine.html'
    extra.write_text('mine', encoding='utf-8')

    result = runner.invoke(app, ['add', 'button', '--sync'], input='')

    assert result.exit_code != 0
    assert extra.is_file(), 'an aborted sync must delete nothing'


def test_sync_leaves_dependencies_alone(project):
    """Syncing allauth must not mirror the components it pulls in."""
    runner.invoke(app, ['add', 'allauth'])
    extra = project / 'templates' / 'cotton' / 'button' / 'mine.html'
    extra.write_text('mine', encoding='utf-8')

    result = runner.invoke(app, ['add', 'allauth', '--sync', '--yes'])

    assert result.exit_code == 0
    assert extra.is_file()


def test_a_component_missing_from_the_install_fails_cleanly(
    project, monkeypatch
):
    """The failure mode that shipping the templates introduces."""
    monkeypatch.setattr(add, 'source_for', lambda name: project / 'gone')

    result = runner.invoke(app, ['add', 'button'])

    assert result.exit_code == 1
    assert 'missing from this installation' in result.stdout
    assert not (project / 'templates').exists()
