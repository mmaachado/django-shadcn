"""Merging downloaded component files into a project.

Kept apart from the download so the behaviour that decides whether a file is
created, kept or replaced can be exercised without touching the network.
"""

import shutil
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path


class WriteMode(Enum):
    """How to treat files that already exist in the project."""

    safe = 'safe'
    overwrite = 'overwrite'
    sync = 'sync'


@dataclass
class MergeResult:
    created: list[Path] = field(default_factory=list)
    skipped: list[Path] = field(default_factory=list)
    overwritten: list[Path] = field(default_factory=list)
    removed: list[Path] = field(default_factory=list)

    @property
    def changed(self) -> bool:
        return bool(self.created or self.overwritten or self.removed)


def _relative_files(directory: Path) -> set[Path]:
    if not directory.is_dir():
        return set()

    return {
        path.relative_to(directory)
        for path in directory.rglob('*')
        if path.is_file()
    }


def obsolete_files(source: Path, destination: Path) -> list[Path]:
    """Files under destination that source no longer provides.

    Only `sync` acts on these; the caller shows them before deleting.
    """
    extra = _relative_files(destination) - _relative_files(source)
    return sorted(destination / path for path in extra)


def merge(source: Path, destination: Path, mode: WriteMode) -> MergeResult:
    """Copy source into destination according to mode.

    `safe` never replaces or deletes anything, which is what makes running
    `add` twice harmless. `sync` mirrors the directory and is the only mode
    that removes files.
    """
    result = MergeResult()

    for relative in sorted(_relative_files(source)):
        target = destination / relative

        if target.exists():
            if mode is WriteMode.safe:
                result.skipped.append(target)
                continue

            shutil.copy2(source / relative, target)
            result.overwritten.append(target)
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / relative, target)
        result.created.append(target)

    if mode is WriteMode.sync:
        for path in obsolete_files(source, destination):
            path.unlink()
            result.removed.append(path)

        _remove_empty_directories(destination)

    return result


def _remove_empty_directories(root: Path) -> None:
    if not root.is_dir():
        return

    directories = sorted(
        (path for path in root.rglob('*') if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    )

    for directory in directories:
        if not any(directory.iterdir()):
            directory.rmdir()
