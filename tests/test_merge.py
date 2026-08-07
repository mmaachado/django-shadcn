"""The three write modes, exercised without touching the network."""

from pathlib import Path

import pytest

from django_shadcn.merge import WriteMode, merge, obsolete_files


@pytest.fixture
def source(tmp_path: Path) -> Path:
    directory = tmp_path / 'source' / 'button'
    (directory / 'nested').mkdir(parents=True)
    (directory / 'index.html').write_text('shipped', encoding='utf-8')
    (directory / 'nested' / 'icon.html').write_text('icon', encoding='utf-8')
    return directory


@pytest.fixture
def destination(tmp_path: Path) -> Path:
    return tmp_path / 'project' / 'templates' / 'cotton' / 'button'


def test_installs_into_an_empty_destination(source, destination):
    result = merge(source, destination, WriteMode.safe)

    assert (destination / 'index.html').read_text(
        encoding='utf-8'
    ) == 'shipped'
    assert (destination / 'nested' / 'icon.html').is_file()
    assert len(result.created) == 2
    assert not result.skipped


def test_safe_mode_keeps_customizations(source, destination):
    """The regression this milestone exists for.

    Re-running `add` used to overwrite whatever the user had changed.
    """
    destination.mkdir(parents=True)
    (destination / 'index.html').write_text('mine', encoding='utf-8')

    result = merge(source, destination, WriteMode.safe)

    assert (destination / 'index.html').read_text(encoding='utf-8') == 'mine'
    assert destination / 'index.html' in result.skipped
    assert destination / 'nested' / 'icon.html' in result.created


def test_safe_mode_never_deletes(source, destination):
    destination.mkdir(parents=True)
    extra = destination / 'mine.html'
    extra.write_text('mine', encoding='utf-8')

    result = merge(source, destination, WriteMode.safe)

    assert extra.is_file()
    assert not result.removed


def test_overwrite_replaces_conflicts_but_keeps_extras(source, destination):
    destination.mkdir(parents=True)
    (destination / 'index.html').write_text('mine', encoding='utf-8')
    extra = destination / 'mine.html'
    extra.write_text('mine', encoding='utf-8')

    result = merge(source, destination, WriteMode.overwrite)

    assert (destination / 'index.html').read_text(
        encoding='utf-8'
    ) == 'shipped'
    assert extra.is_file(), 'overwrite must not delete unrelated files'
    assert destination / 'index.html' in result.overwritten
    assert not result.removed


def test_sync_mirrors_the_directory(source, destination):
    destination.mkdir(parents=True)
    (destination / 'index.html').write_text('mine', encoding='utf-8')
    extra = destination / 'mine.html'
    extra.write_text('mine', encoding='utf-8')

    result = merge(source, destination, WriteMode.sync)

    assert (destination / 'index.html').read_text(
        encoding='utf-8'
    ) == 'shipped'
    assert not extra.exists()
    assert extra in result.removed


def test_sync_drops_directories_left_empty(source, destination):
    stale = destination / 'old'
    stale.mkdir(parents=True)
    (stale / 'gone.html').write_text('gone', encoding='utf-8')

    merge(source, destination, WriteMode.sync)

    assert not stale.exists()


def test_obsolete_files_lists_what_sync_would_remove(source, destination):
    destination.mkdir(parents=True)
    (destination / 'index.html').write_text('mine', encoding='utf-8')
    extra = destination / 'mine.html'
    extra.write_text('mine', encoding='utf-8')

    assert obsolete_files(source, destination) == [extra]


def test_obsolete_files_is_empty_for_a_missing_destination(
    source, destination
):
    assert obsolete_files(source, destination) == []


def test_syncing_a_component_that_ships_nothing_creates_nothing(
    tmp_path, destination
):
    """Sync prunes empty directories, and there may be none to prune."""
    empty = tmp_path / 'source' / 'empty'
    empty.mkdir(parents=True)

    result = merge(empty, destination, WriteMode.sync)

    assert not result.changed
    assert not destination.exists()
