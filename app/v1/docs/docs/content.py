"""Pages are Markdown files that may embed cotton components.

Markdown runs first and leaves any <c-...> block alone, then the result goes
through the cotton compiler and the template engine. Fenced code is wrapped in
{% verbatim %} on the way, so an example can show Django tags without the
engine executing them.
"""

import re

import markdown
from django.conf import settings
from django.template import Context, Template
from django.utils.safestring import mark_safe
from django.utils.translation import get_language
from django_cotton.compiler_regex import CottonCompiler

CONTENT_ROOT = settings.BASE_DIR / "content"

EXTENSIONS = ["fenced_code", "tables", "attr_list", "sane_lists"]

FRONT_MATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
CODE_BLOCK = re.compile(r"<pre>.*?</pre>", re.DOTALL)


class PageNotFound(Exception):
    pass


def _parser():
    parser = markdown.Markdown(extensions=EXTENSIONS)
    is_block_level = parser.is_block_level

    # Markdown has never heard of the cotton tags and would wrap them in <p>.
    parser.is_block_level = lambda tag: tag.startswith("c-") or is_block_level(tag)

    return parser


def _split_front_matter(text):
    match = FRONT_MATTER.match(text)
    if not match:
        return {}, text

    meta = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if separator:
            meta[key.strip()] = value.strip()

    return meta, text[match.end() :]


def _localize(meta):
    """Resolve front matter keys carrying a language suffix.

        description: An image element with a fallback.
        description.pt-br: Uma imagem com fallback.

    The suffixed value wins when it matches the active language, and the bare
    key is what the rest of the code sees either way.
    """
    language = get_language() or "en"
    resolved = {}

    for key, value in meta.items():
        base, _, suffix = key.rpartition(".")

        if not base:
            resolved.setdefault(key, value)
        elif suffix == language:
            resolved[base] = value

    return resolved


def source(slug):
    """Return the front matter and the raw Markdown body of a page.

    A page translated into the active language wins; anything untranslated
    falls back to English rather than disappearing.
    """
    language = get_language() or "en"
    candidates = [CONTENT_ROOT / language / f"{slug}.md"]
    candidates.append(CONTENT_ROOT / f"{slug}.md")

    for path in candidates:
        if path.is_file():
            meta, body = _split_front_matter(path.read_text(encoding="utf-8"))
            return _localize(meta), body

    raise PageNotFound(slug)


def render(slug, context=None):
    """Return the front matter and the rendered body of a content page."""
    meta, body = source(slug)

    html = _parser().convert(body)
    html = CODE_BLOCK.sub(
        lambda match: (
            "<c-docs.code-block>{% verbatim %}"
            + match.group(0)
            + "{% endverbatim %}</c-docs.code-block>"
        ),
        html,
    )

    if "<c-" in html:
        html = CottonCompiler().process(html)

    return meta, mark_safe(Template(html).render(Context(context or {})))
