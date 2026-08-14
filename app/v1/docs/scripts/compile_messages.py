"""Compile locale/**/django.po into the .mo files Django reads at runtime.

Django's own compilemessages shells out to GNU gettext, which is not present
on every machine and is not present on the deployment builder either. This
does the same job in pure Python, so the .mo files can be produced anywhere
and committed alongside the .po they came from.

    python scripts/compile_messages.py
"""

from pathlib import Path

import polib

LOCALE_ROOT = Path(__file__).resolve().parent.parent / "locale"


def main():
    catalogs = sorted(LOCALE_ROOT.glob("*/LC_MESSAGES/django.po"))

    if not catalogs:
        raise SystemExit(f"no catalogs under {LOCALE_ROOT}")

    for source in catalogs:
        target = source.with_suffix(".mo")
        polib.pofile(str(source)).save_as_mofile(str(target))
        print(f"wrote {target.relative_to(LOCALE_ROOT.parent)}")


if __name__ == "__main__":
    main()
