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


def test_declining_the_sync_prompt_deletes_nothing(project):
    runner.invoke(app, ['add', 'button'])
    extra = project / 'templates' / 'cotton' / 'button' / 'mine.html'
    extra.write_text('mine', encoding='utf-8')

    result = runner.invoke(app, ['add', 'button', '--sync'], input='n\n')

    assert result.exit_code != 0
    assert extra.is_file()


def test_sync_with_nothing_to_remove_never_prompts(project):
    """The prompt exists for deletions; without any it must not appear."""
    runner.invoke(app, ['add', 'button'])

    result = runner.invoke(app, ['add', 'button', '--sync'], input='')

    assert result.exit_code == 0
    assert 'Continue?' not in result.stdout


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


def test_add_names_the_alpine_plugin_a_component_needs(project):
    """Without this the component installs, renders, and never animates."""
    result = runner.invoke(app, ['add', 'accordion'])

    assert result.exit_code == 0
    assert '@alpinejs/collapse' in result.stdout


def test_the_plugin_is_named_once_for_the_whole_run(project):
    result = runner.invoke(app, ['add', 'accordion', 'collapsible'])

    assert result.exit_code == 0
    assert result.stdout.count('@alpinejs/collapse') == 1


def test_a_component_needing_no_plugin_says_nothing(project):
    result = runner.invoke(app, ['add', 'button'])

    assert '@alpinejs' not in result.stdout


def test_a_component_missing_from_the_install_fails_cleanly(
    project, monkeypatch
):
    """The failure mode that shipping the templates introduces."""
    monkeypatch.setattr(add, 'source_for', lambda name: project / 'gone')

    result = runner.invoke(app, ['add', 'button'])

    assert result.exit_code == 1
    assert 'missing from this installation' in result.stdout
    assert not (project / 'templates').exists()


def test_a_misspelled_name_gets_a_suggestion(project):
    result = runner.invoke(app, ['add', 'buton'])

    assert result.exit_code == 1
    assert 'button' in result.stdout


def test_an_unknown_name_no_longer_dumps_the_registry(project):
    """The old message answered a typo with all 57 names."""
    result = runner.invoke(app, ['add', 'qqqq'])

    assert result.exit_code == 1
    assert 'tooltip' not in result.stdout
    assert 'aspect_ratio' not in result.stdout


def test_the_unknown_message_agrees_in_number(project):
    one = runner.invoke(app, ['add', 'qqqq'])
    two = runner.invoke(app, ['add', 'qqqq', 'wwww'])

    assert 'Unknown component:' in one.stdout
    assert 'Unknown components:' in two.stdout


def test_a_capitalized_name_installs(project):
    result = runner.invoke(app, ['add', 'BUTTON'])

    assert result.exit_code == 0
    assert (project / BUTTON).is_file()


def test_dry_run_writes_nothing(project):
    result = runner.invoke(app, ['add', 'button', '--dry-run'])

    assert result.exit_code == 0
    assert 'would add button' in result.stdout
    assert not (project / 'templates').exists()


def test_dry_run_lists_what_sync_would_remove(project):
    runner.invoke(app, ['add', 'allauth'])
    extra = project / 'templates' / 'account' / 'mine.html'
    extra.write_text('mine', encoding='utf-8')

    result = runner.invoke(app, ['add', 'allauth', '--sync', '--dry-run'])

    assert result.exit_code == 0
    assert 'removed' in result.stdout
    assert extra.is_file(), 'a dry run must delete nothing'


def test_dry_run_never_prompts(project):
    """The preview is the answer the prompt was asking for."""
    runner.invoke(app, ['add', 'button'])
    extra = project / 'templates' / 'cotton' / 'button' / 'mine.html'
    extra.write_text('mine', encoding='utf-8')

    result = runner.invoke(
        app, ['add', 'button', '--sync', '--dry-run'], input=''
    )

    assert result.exit_code == 0
    assert 'Continue?' not in result.stdout
    assert extra.is_file()


def test_the_preview_names_the_same_files_the_real_run_writes(project):
    preview = runner.invoke(app, ['add', 'combobox', '--dry-run'])
    real = runner.invoke(app, ['add', 'combobox'])

    def created(output: str) -> list[str]:
        return [line for line in output.splitlines() if 'created' in line]

    assert created(preview.stdout)
    assert created(preview.stdout) == created(real.stdout)


@pytest.mark.parametrize('flags', [[], ['--overwrite'], ['--sync', '--yes']])
def test_a_directory_where_a_file_belongs_stops_the_run(project, flags):
    """copy2 would write index.html/index.html and call it overwritten."""
    (project / 'templates' / 'cotton' / 'button' / 'index.html').mkdir(
        parents=True
    )

    result = runner.invoke(app, ['add', 'button', *flags])

    assert result.exit_code == 1
    assert 'paths in the way' in result.stdout
    assert not (
        project
        / 'templates'
        / 'cotton'
        / 'button'
        / 'index.html'
        / 'index.html'
    ).exists()


def test_a_file_where_a_directory_belongs_stops_the_run(project):
    """This one used to surface as a raw FileExistsError."""
    icon = project / 'templates' / 'cotton' / 'icon'
    icon.parent.mkdir(parents=True)
    icon.write_text('mine', encoding='utf-8')

    result = runner.invoke(app, ['add', 'accordion'])

    assert result.exit_code == 1
    assert 'paths in the way' in result.stdout
    assert icon.read_text(encoding='utf-8') == 'mine'


def test_a_conflict_in_a_dependency_writes_nothing_at_all(project):
    """The reason the check runs before the loop and not inside it."""
    icon = project / 'templates' / 'cotton' / 'icon'
    icon.parent.mkdir(parents=True)
    icon.write_text('mine', encoding='utf-8')

    result = runner.invoke(app, ['add', 'accordion'])

    assert result.exit_code == 1
    assert not (project / 'templates' / 'cotton' / 'accordion').exists()
