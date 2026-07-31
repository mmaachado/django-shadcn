"""Fail the release if the built artifact does not match the tag.

Without the full tag history, hatch-vcs silently falls back to a development
version and the wrong package would be published.
"""

import sys
from pathlib import Path

from packaging.version import InvalidVersion, Version


def built_version() -> str:
    sdists = list(Path('dist').glob('*.tar.gz'))
    if len(sdists) != 1:
        sys.exit(f'expected one sdist in dist/, found {len(sdists)}')

    name = sdists[0].name
    return name.removeprefix('django_shadcn-').removesuffix('.tar.gz')


def main(tag: str) -> None:
    built = built_version()

    try:
        # Compare parsed versions: the tag may not be in canonical form,
        # and v1.0.0-rc2 builds as 1.0.0rc2.
        expected = Version(tag.removeprefix('v'))
    except InvalidVersion:
        sys.exit(f'tag {tag} is not a valid version')

    if expected != Version(built):
        sys.exit(f'tag {tag} does not match the built version {built}')

    print(f'built {built} from tag {tag}')


if __name__ == '__main__':
    main(sys.argv[1])
