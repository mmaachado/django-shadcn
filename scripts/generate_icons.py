"""Regenerate the lucide icon partials used by the components.

Scans the components for <c-icon name="..."> and writes one partial per icon
under components/icon/, holding just the shapes that go inside the <svg> shell
in components/icon/index.html.

Run it after adding an icon to a component:

    python scripts/generate_icons.py

Needs network access, so it stays out of pull request CI.
"""

import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

LUCIDE_VERSION = '1.28.0'
ICON_URL = 'https://unpkg.com/lucide-static@{version}/icons/{name}.svg'

REPO_ROOT = Path(__file__).resolve().parent.parent
COMPONENTS_ROOT = REPO_ROOT / 'components'
ICON_ROOT = COMPONENTS_ROOT / 'icon'

USAGE = re.compile(r'<c-icon\s[^>]*name=[\'"]([a-z0-9-]+)[\'"]')

# Everything between the opening <svg ...> and </svg>.
SVG_BODY = re.compile(r'<svg[^>]*>(.*)</svg>', re.DOTALL)


def used_icons() -> set[str]:
    names: set[str] = set()

    for template in COMPONENTS_ROOT.rglob('*.html'):
        names.update(USAGE.findall(template.read_text(encoding='utf-8')))

    return names


def fetch(name: str) -> str:
    url = ICON_URL.format(version=LUCIDE_VERSION, name=name)

    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            svg = response.read().decode('utf-8')
    except urllib.error.HTTPError as error:
        if error.code == 404:
            sys.exit(f'no lucide icon named {name}')
        raise

    body = SVG_BODY.search(svg)
    if not body:
        sys.exit(f'unexpected svg markup for {name}')

    shapes = [line.strip() for line in body.group(1).strip().splitlines()]

    return '\n'.join(shapes) + '\n'


def partial_for(name: str) -> Path:
    # Cotton resolves <c-icon.chevron-down> to icon/chevron_down.html.
    return ICON_ROOT / f'{name.replace("-", "_")}.html'


def main() -> None:
    names = used_icons()

    if not names:
        sys.exit('no <c-icon name="..."> found in components/')

    ICON_ROOT.mkdir(parents=True, exist_ok=True)
    wanted = {partial_for(name) for name in names}

    for name in sorted(names):
        partial_for(name).write_text(fetch(name), encoding='utf-8')
        print(f'wrote {partial_for(name).relative_to(REPO_ROOT)}')

    for existing in ICON_ROOT.glob('*.html'):
        if existing.name != 'index.html' and existing not in wanted:
            existing.unlink()
            print(f'removed {existing.relative_to(REPO_ROOT)}')


if __name__ == '__main__':
    main()
