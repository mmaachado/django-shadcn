"""Copy the library's components into this tree, for the deploy to read.

The pages render components/ out of the library this project sits in, which
is what keeps them from drifting from what the CLI installs. A deploy has no
library above it: the host builds from this directory, and only what ends up
inside it is bundled. So the build copies the components in, and settings.py
falls back to that copy when there is no library to be found.

Nothing this writes is committed. The copy is gitignored, and a checkout
always has the real library above it, which wins. Run it by hand only to
reproduce what the deploy sees.

    python scripts/sync_components.py
"""

import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TARGET = BASE_DIR / "components"


def library():
    """The checkout this project sits inside, however deep that turns out.

    Counting directories upwards was fine while this was a direct child of
    the library root, and stopped being fine the moment it moved. Looking for
    the thing being copied is the version that survives the next move.
    """
    for candidate in BASE_DIR.parents:
        components = candidate / "components"
        if components.is_dir() and (candidate / "pyproject.toml").is_file():
            return components

    return None


def main():
    source = library()

    if source is None:
        raise SystemExit(
            f"no library components above {BASE_DIR}. The build needs the "
            "whole repository: on Vercel that is 'Include source files "
            "outside of the Root Directory in the Build Step'."
        )

    shutil.rmtree(TARGET, ignore_errors=True)
    shutil.copytree(source, TARGET)
    print(f"synced {len(list(TARGET.glob('*/index.html')))} components")


if __name__ == "__main__":
    main()
