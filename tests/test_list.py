"""What `list` counts as installed.

The destination directory existing says nothing on its own: `allauth`
shares templates/account/ with django-allauth itself.
"""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from django_shadcn import list as list_command
from django_shadcn.list import is_installed
from django_shadcn.main import app

runner = CliRunner()


@pytest.fixture
def project(tmp_path: Path, monkeypatch) -> Path:
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_nothing_is_installed_in_an_empty_project(project):
    assert not is_installed('button')
    assert not is_installed('allauth')


def test_a_component_is_installed_once_add_has_run(project):
    runner.invoke(app, ['add', 'button'])

    assert is_installed('button')


def test_a_third_party_account_directory_is_not_allauth(project):
    """The false positive this exists to kill.

    login.html is a name our component and django-allauth both use, so
    matching on any single shipped file would call this installed.
    """
    account = project / 'templates' / 'account'
    account.mkdir(parents=True)
    (account / 'login.html').write_text('mine', encoding='utf-8')

    assert not is_installed('allauth')


def test_a_partial_install_reads_as_not_installed(project):
    """Deliberate bias: a redundant add is cheaper than a skipped one."""
    runner.invoke(app, ['add', 'allauth'])
    (project / 'templates' / 'account' / 'signup.html').unlink()

    assert not is_installed('allauth')


def test_a_customized_component_is_still_installed(project):
    """Owning the code is the point; editing it cannot un-install it."""
    runner.invoke(app, ['add', 'button'])
    index = project / 'templates' / 'cotton' / 'button' / 'index.html'
    index.write_text('mine', encoding='utf-8')

    assert is_installed('button')


def test_allauth_is_installed_once_add_has_run(project):
    runner.invoke(app, ['add', 'allauth'])

    assert is_installed('allauth')


def test_an_empty_destination_directory_does_not_count(project):
    (project / 'templates' / 'cotton' / 'button').mkdir(parents=True)

    assert not is_installed('button')


def test_an_unrelated_file_in_the_destination_does_not_count(project):
    """A folder named after a component is not the component."""
    destination = project / 'templates' / 'cotton' / 'button'
    destination.mkdir(parents=True)
    (destination / 'notes.md').write_text('mine', encoding='utf-8')

    assert not is_installed('button')


def test_a_component_that_ships_nothing_is_not_installed(project, monkeypatch):
    """all() of an empty sequence is True, which would report every
    component installed in every project."""
    empty = project / 'empty'
    empty.mkdir()
    monkeypatch.setattr(list_command, 'source_for', lambda name: empty)

    assert not is_installed('button')


def test_the_panel_reports_the_installed_count(project):
    runner.invoke(app, ['add', 'button'])

    result = runner.invoke(app, ['list'])

    assert result.exit_code == 0
    assert 'installed' in result.stdout
