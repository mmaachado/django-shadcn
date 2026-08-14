"""Plain-text views of the documentation, for models that read the site.

Follows the llms.txt convention: llms.txt is an index, llms-full.txt carries
the whole thing inline. Both come from the same Markdown the site renders, so
they cannot drift from it.
"""

import re

from django.http import HttpResponse
from django.urls import reverse

from .content import source
from .nav import NAV

SUMMARY = (
    "django-shadcn is an unofficial Django port of shadcn/ui. It ships as a "
    "CLI that copies django-cotton templates into your project, so the "
    "components become your code rather than a dependency. Components are "
    "written with Tailwind CSS v4 and Alpine.js."
)

# The rendered demos repeat what the code examples already show, and only add
# noise for a reader that cannot see them.
DEMO = re.compile(
    r"<c-docs\.demo-section.*?</c-docs\.demo-section>\n*", re.DOTALL
)


def _plain(text):
    return HttpResponse(text, content_type="text/plain; charset=utf-8")


def llms_txt(request):
    def absolute(name, **kwargs):
        return request.build_absolute_uri(reverse(name, kwargs=kwargs))

    lines = ["# django-shadcn", "", f"> {SUMMARY}", ""]

    for section, entries in NAV:
        lines += [f"## {section}", ""]
        for slug, label in entries:
            meta, _ = source(slug)
            url = absolute("page", slug=slug)
            lines.append(f"- [{label}]({url}): {meta.get('description', '')}")
        lines.append("")

    lines += [
        "## Optional",
        "",
        f"- [Full documentation]({absolute('llms-full')}): every page above, "
        "inlined as Markdown",
        "",
    ]

    return _plain("\n".join(lines))


def llms_full_txt(request):
    parts = ["# django-shadcn", "", SUMMARY, ""]

    for _, entries in NAV:
        for slug, _label in entries:
            meta, body = source(slug)
            parts += [
                "---",
                "",
                f"# {meta.get('title', slug)}",
                "",
                f"> {meta.get('description', '')}",
                "",
                DEMO.sub("", body).strip(),
                "",
            ]

    return _plain("\n".join(parts))
