from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
COMPONENTS_ROOT = REPO_ROOT / 'components'


@pytest.fixture(scope='session')
def components_root() -> Path:
    return COMPONENTS_ROOT


@pytest.fixture(scope='session')
def component_names() -> list[str]:
    """Component directory names, sorted."""
    return sorted(
        path.name for path in COMPONENTS_ROOT.iterdir() if path.is_dir()
    )


@pytest.fixture(scope='session')
def component_templates() -> list[Path]:
    return sorted(COMPONENTS_ROOT.rglob('*.html'))
