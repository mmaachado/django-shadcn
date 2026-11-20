"""Compare two builds of the stylesheet.

The class names are compared first, since a list of missing and stale classes
is what tells a contributor which component changed. When the names match, the
two texts are compared with line endings normalised, which catches a changed
declaration or token.

    python scripts/check_stylesheet.py static/css/output.css <new build>
"""

import re
import sys
from pathlib import Path

# An escape is one character, or a hex code point with an optional trailing
# space. Tailwind writes a leading digit that way: 2xl:flex becomes
# .\32 xl\:flex.
ESCAPE = r"\\(?:[0-9a-fA-F]{1,6} ?|.)"
CLASS = re.compile(rf"\.(-?(?:[A-Za-z_]|{ESCAPE})(?:{ESCAPE}|[\w-])*)")


def classes(css):
    return set(CLASS.findall(css))


def main():
    committed_path, build_path = sys.argv[1:3]
    committed_text = Path(committed_path).read_text(encoding="utf-8")
    build_text = Path(build_path).read_text(encoding="utf-8")
    committed = classes(committed_text)
    build = classes(build_text)

    rebuild = (
        f"{committed_path} is out of date. Rebuild it, from "
        "app/v1/docs:\nnpx @tailwindcss/cli -i assets/input.css "
        "-o static/css/output.css"
    )

    if committed == build:
        # read_text turns \r\n into \n, so a Windows checkout compares equal.
        if committed_text != build_text:
            raise SystemExit(
                f"same classes, but the CSS differs\n{rebuild}"
            )
        print(f"{len(committed)} classes, {committed_path} is up to date")
        return

    missing = sorted(build - committed)
    stale = sorted(committed - build)

    def unescape(name):
        return re.sub(
            r"\\(?:([0-9a-fA-F]{1,6}) ?|(.))",
            lambda match: chr(int(match[1], 16)) if match[1] else match[2],
            name,
        )

    if missing:
        print("missing (in the build, not in the committed file):")
        for name in missing[:20]:
            print(f"  {unescape(name)}")

    if stale:
        print("stale (in the committed file, not in the build):")
        for name in stale[:20]:
            print(f"  {unescape(name)}")

    raise SystemExit(rebuild)


if __name__ == "__main__":
    main()
