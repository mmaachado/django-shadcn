"""The attribute reference of a component, read from its templates.

A component declares its attributes and their defaults in <c-vars>, and the
values it understands are the ones its markup branches on:

    <c-vars class="" variant="default" size="default"></c-vars>
    {% if variant == 'default' %}...{% elif variant == 'outline' %}...

Read from there, the reference cannot fall behind the component.
"""

import re

from django.conf import settings
from django.utils.translation import gettext as _

CVARS = re.compile(r"<c-vars\b([^>]*)>")
ATTRIBUTE = re.compile(r'([\w-]+)(?:\s*=\s*"([^"]*)")?')
BRANCH = re.compile(r"\{%\s*(?:el)?if\s+(\w+)\s*==\s*'([^']*)'\s*%\}")

# On every part, so it is said once under the table instead of on each row.
COMMON = {"class"}


def tag_for(component, path):
    """The cotton tag a template answers to: button/index.html is
    <c-button>, card/header.html is <c-card.header>."""
    name = component.replace("_", "-")
    if path.stem == "index":
        return f"c-{name}"
    return f"c-{name}.{path.stem.replace('_', '-')}"


def attributes(source):
    """[(name, default, values)] declared by one template, in order.

    A bare attribute in <c-vars> has no default. Values are what the
    template compares the attribute against, the default included.
    """
    declared = CVARS.search(source)
    if not declared:
        return []

    branches = {}
    for name, value in BRANCH.findall(source):
        branches.setdefault(name, [])
        if value not in branches[name]:
            branches[name].append(value)

    rows = []
    for name, default in ATTRIBUTE.findall(declared.group(1)):
        if name in COMMON:
            continue
        values = list(branches.get(name, []))
        if default and values and default not in values:
            values.insert(0, default)
        rows.append((name, default, values))
    return rows


def parts(component):
    """[(tag, rows)] for the component and each of its parts, root first."""
    directory = settings.COMPONENTS_DIR / component
    paths = sorted(
        directory.glob("*.html"),
        key=lambda path: (path.stem != "index", path.stem),
    )
    return [
        (tag_for(component, path), attributes(path.read_text(encoding="utf-8")))
        for path in paths
    ]


def table(component):
    """The reference as a Markdown table, in the active language."""

    def code(text):
        return f"`{text}`" if text else "—"

    lines = [
        f"| {_('Tag')} | {_('Attribute')} | {_('Default')} | {_('Values')} |",
        "| --- | --- | --- | --- |",
    ]
    for tag, rows in parts(component):
        for name, default, values in rows:
            lines.append(
                f"| `<{tag}>` | `{name}` | {code(default)} | "
                f"{', '.join(code(value) for value in values) or '—'} |"
            )

    if len(lines) == 2:
        lines = []
    lines.append(
        "\n"
        + _(
            "Every part also takes `class`, added to its own classes, and "
            "passes any other attribute on to its element."
        )
    )
    return "\n".join(lines).strip()
