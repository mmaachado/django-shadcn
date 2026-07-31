import sys

from rich.console import Console


def _use_utf8(stream) -> None:
    """Let the output carry emoji on a legacy Windows code page.

    Without this, printing the panels below dies with UnicodeEncodeError on a
    cp1252 console.
    """
    if hasattr(stream, 'reconfigure'):
        try:
            stream.reconfigure(encoding='utf-8', errors='replace')
        except (OSError, ValueError):
            pass


_use_utf8(sys.stdout)
_use_utf8(sys.stderr)

console = Console()
