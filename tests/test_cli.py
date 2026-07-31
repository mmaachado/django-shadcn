"""CLI smoke tests.

Kept free of network access: `init` and `add` clone the component
repository through copier, which does not belong in the test suite.
"""

from typer.testing import CliRunner

from django_shadcn.components import dependencies
from django_shadcn.main import app

runner = CliRunner()


def test_help_lists_the_commands():
    result = runner.invoke(app, ['--help'])

    assert result.exit_code == 0
    for command in ('init', 'add', 'list'):
        assert command in result.stdout


def test_list_prints_every_component():
    result = runner.invoke(app, ['list'])

    assert result.exit_code == 0
    # Rich wraps the panel into columns, so check names, not layout.
    for component in dependencies:
        assert component in result.stdout


def test_add_without_arguments_shows_usage():
    result = runner.invoke(app, ['add'])

    # Click writes usage errors to stderr and exits with 2.
    assert result.exit_code == 2
    assert 'Usage' in result.stderr
