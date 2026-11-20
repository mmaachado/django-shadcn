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

# :::pt-br opens a language inside a passage, a bare ::: closes the passage.
PASSAGE = re.compile(r"^:::([a-z]{2}(?:-[a-z]+)?)?[ \t]*$")
FENCE = re.compile(r"^(```|~~~)")
DEMO_OPEN = re.compile(r"^<c-docs\.(?:demo-section|example|cheat-sheet)\b")
DEMO_CLOSE = re.compile(r"</c-docs\.(?:demo-section|example|cheat-sheet)>")

# The attribute reference of a component, generated from its templates.
REFERENCE = re.compile(
    r'^<c-docs\.api-reference name="(?P<name>[\w-]+)"\s*/>[ \t]*$', re.MULTILINE
)

# The tag, the parts, the root's attributes and a snippet, near the top.
CHEAT_SHEET = re.compile(
    r'^<c-docs\.cheat-sheet name="(?P<name>[\w-]+)">[ \t]*\n'
    r"(?P<snippet>.*?)\n"
    r"</c-docs\.cheat-sheet>[ \t]*$",
    re.DOTALL | re.MULTILINE,
)

# A demo written once: rendered, and shown below as its own source.
EXAMPLE = re.compile(
    r"^<c-docs\.example(?P<attrs>[^>]*)>[ \t]*\n"
    r"(?P<source>.*?)\n"
    r"</c-docs\.example>[ \t]*$",
    re.DOTALL | re.MULTILINE,
)


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


class PassageError(ValueError):
    pass


def _passages(body):
    """Split a body into markup and translated passages, in order.

    Prose that has a translation is written as a passage, one block per
    language, closed by a bare marker:

        :::en
        ## Usage
        :::pt-br
        ## Uso
        :::

    Everything outside a passage, the demos and the fenced code above all, is
    written once and shared by every language. Yields ("text", str) for that
    and ("passage", {language: str}) for each passage.
    """
    languages = {code for code, _name in settings.LANGUAGES}
    text, passage, current, fence = [], None, None, None

    for number, line in enumerate(body.splitlines(keepends=True), 1):
        marker = PASSAGE.match(line)
        opens_fence = FENCE.match(line)

        if fence:
            if line.strip() == fence:
                fence = None
        elif opens_fence or DEMO_OPEN.match(line):
            if opens_fence:
                fence = opens_fence.group(1)
            if passage is not None:
                raise PassageError(
                    f"line {number}: demos and fenced code belong outside a "
                    "passage, written once for every language"
                )
        elif marker and marker.group(1):
            language = marker.group(1)
            if language not in languages:
                raise PassageError(
                    f"line {number}: unknown language {language}"
                )
            if passage is None:
                if text:
                    yield "text", "".join(text)
                    text = []
                passage = {}
            if language in passage:
                raise PassageError(f"line {number}: {language} given twice")
            passage[language] = []
            current = language
            continue
        elif marker:
            if passage is None:
                raise PassageError(f"line {number}: ::: closes no passage")
            if "en" not in passage:
                raise PassageError(f"line {number}: a passage needs English")
            yield "passage", {
                key: "".join(lines) for key, lines in passage.items()
            }
            passage, current = None, None
            continue

        if passage is None:
            text.append(line)
        else:
            passage[current].append(line)

    if passage is not None:
        raise PassageError("a passage is never closed with :::")
    if text:
        yield "text", "".join(text)


def _translate(body, language):
    """The body in one language, English wherever a passage lacks it."""
    return "".join(
        payload if kind == "text" else payload.get(language, payload["en"])
        for kind, payload in _passages(body)
    )


def _override(slug, language):
    return CONTENT_ROOT / language / f"{slug}.md"


def _read(path):
    return _split_front_matter(path.read_text(encoding="utf-8"))


def source(slug):
    """Return the front matter and the raw Markdown body of a page.

    A whole-file override in content/<language>/ wins, for the pages that are
    nearly all prose. Otherwise the English file is read, and its passages
    resolve to the active language; anything untranslated falls back to
    English rather than disappearing.
    """
    language = get_language() or "en"
    override = _override(slug, language)
    path = override if override.is_file() else CONTENT_ROOT / f"{slug}.md"

    if not path.is_file():
        raise PageNotFound(slug)

    meta, body = _read(path)
    body = _expand_examples(_translate(body, language))
    return _localize(meta), _expand_references(body)


def _expand_references(body):
    from .reference import cheat_sheet, table

    body = CHEAT_SHEET.sub(
        lambda match: cheat_sheet(
            match.group("name").replace("-", "_"), match.group("snippet")
        ),
        body,
    )
    return REFERENCE.sub(
        lambda match: table(match.group("name").replace("-", "_")), body
    )


def _expand_examples(body):
    """Turn each <c-docs.example> into the demo and a fenced copy of it.

    Both halves come from the same text, so the code a reader copies is the
    code that rendered above it. The fence is wrapped in {% verbatim %} by
    render(), which leaves Django tags in the source visible. Blank lines are
    dropped from the demo half only: Markdown would end the HTML block there.
    """

    def expand(match):
        source = match.group("source")
        demo = "\n".join(line for line in source.splitlines() if line.strip())
        return (
            f"<c-docs.demo-section{match.group('attrs')}>\n{demo}\n"
            f"</c-docs.demo-section>\n\n```html\n{source}\n```"
        )

    return EXAMPLE.sub(expand, body)


def _is_prose(line):
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith(("<", "{%"))


def untranslated(slug, language):
    """English prose a reader of the language would see, first line of each
    paragraph. Empty when the page is fully translated."""
    if language == "en" or _override(slug, language).is_file():
        return []

    meta, body = _read(CONTENT_ROOT / f"{slug}.md")
    missing = missing_prose(body, language)
    if "description" in meta and f"description.{language}" not in meta:
        missing.insert(0, f"description: {meta['description']}")
    return missing


def coverage(language):
    """Every page in the sidebar that still shows English to a reader of the
    language, with the passages it lacks."""
    from .nav import SLUGS

    report = {slug: untranslated(slug, language) for slug in SLUGS}
    return {slug: missing for slug, missing in report.items() if missing}


def missing_prose(body, language):
    """The English prose of a body that has no passage in the language."""
    missing = []

    for kind, payload in _passages(body):
        if kind == "passage":
            if language not in payload:
                prose = [
                    line.strip()
                    for line in payload["en"].splitlines()
                    if _is_prose(line)
                ]
                missing += prose[:1]
            continue

        demo = fence = paragraph = False
        for line in payload.splitlines():
            if fence:
                fence = not FENCE.match(line)
            elif FENCE.match(line):
                fence = True
            elif DEMO_OPEN.match(line):
                demo = not DEMO_CLOSE.search(line)
            elif demo:
                demo = not DEMO_CLOSE.search(line)
            elif _is_prose(line) and not paragraph:
                missing.append(line.strip())
            paragraph = (
                _is_prose(line)
                and not (fence or demo)
                and not FENCE.match(line)
            )

    return missing


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
