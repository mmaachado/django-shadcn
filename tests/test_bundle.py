"""Locating the templates that ship with the package.

The wheel gets them through a force-include; a source checkout has them at
the repository root. Both paths have to keep working, and the registry has
to agree with whichever one is in use.
"""

import tomllib
from pathlib import Path

import pytest

from django_shadcn import bundle
from django_shadcn.bundle import components_root, source_for
from django_shadcn.components import registry
from django_shadcn.initialize import THEME_FILE

REPO_ROOT = Path(__file__).resolve().parent.parent
WHEEL_DESTINATION = 'django_shadcn/_components'


def test_every_registered_component_ships_with_the_package():
    missing = [name for name in registry if not source_for(name).is_dir()]

    assert not missing, f'registered but not shipped: {missing}'


def test_the_theme_file_ships_with_the_package():
    assert (components_root() / THEME_FILE).is_file()


def test_a_checkout_resolves_to_the_repository_tree():
    assert components_root() == REPO_ROOT / 'components'


def test_the_bundled_directory_wins_over_the_checkout(tmp_path, monkeypatch):
    """An installed wheel must never read from somewhere else on disk."""
    bundled = tmp_path / '_components'
    bundled.mkdir()
    monkeypatch.setattr(bundle, '_BUNDLED', bundled)

    assert components_root() == bundled


def test_a_missing_installation_fails_loudly(tmp_path, monkeypatch):
    monkeypatch.setattr(bundle, '_BUNDLED', tmp_path / 'nowhere')
    monkeypatch.setattr(bundle, '_CHECKOUT', tmp_path / 'also-nowhere')

    with pytest.raises(RuntimeError):
        components_root()


def test_the_wheel_is_configured_to_carry_the_components():
    """Without this mapping the wheel installs a registry and no templates."""
    config = tomllib.loads(
        (REPO_ROOT / 'pyproject.toml').read_text(encoding='utf-8')
    )
    wheel = config['tool']['hatch']['build']['targets']['wheel']

    assert wheel.get('force-include', {}).get('components') == (
        WHEEL_DESTINATION
    ), 'the wheel would install the registry with no templates behind it'
