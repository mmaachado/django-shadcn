"""`init`, run against the templates that ship with the package."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from django_shadcn.constants import DEFAULT_COMPONENTS_DIRECTORY
from django_shadcn.initialize import THEME_FILE
from django_shadcn.main import app

runner = CliRunner()


@pytest.fixture
def project(tmp_path: Path, monkeypatch) -> Path:
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_creates_the_components_directory(project):
    result = runner.invoke(app, ['init'])

    assert result.exit_code == 0
    assert (project / DEFAULT_COMPONENTS_DIRECTORY).is_dir()


def test_writes_the_theme_file(project):
    result = runner.invoke(app, ['init'])

    assert result.exit_code == 0
    assert (project / THEME_FILE).read_text(encoding='utf-8').strip()


def test_running_twice_keeps_the_theme_file(project):
    """It used to prompt here, under a spinner, and raise without a tty."""
    runner.invoke(app, ['init'])
    (project / THEME_FILE).write_text('mine', encoding='utf-8')

    result = runner.invoke(app, ['init'])

    assert result.exit_code == 0
    assert (project / THEME_FILE).read_text(encoding='utf-8') == 'mine'


def test_force_replaces_the_theme_file(project):
    runner.invoke(app, ['init'])
    (project / THEME_FILE).write_text('mine', encoding='utf-8')

    result = runner.invoke(app, ['init', '--force'])

    assert result.exit_code == 0
    assert (project / THEME_FILE).read_text(encoding='utf-8') != 'mine'


def test_reports_which_of_the_two_happened(project):
    created = runner.invoke(app, ['init'])
    kept = runner.invoke(app, ['init'])

    assert 'Added' in created.stdout
    assert 'Kept' in kept.stdout
