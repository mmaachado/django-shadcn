"""Request every public page of the portal, in every language.

A template error in content/, a broken nav.py entry or a missing static
manifest would otherwise only show up after the deploy. Run collectstatic
first: the storage backend raises when the manifest is missing.
"""

import io
import re
import sys
import tempfile
from pathlib import Path
from unittest import mock

from django.conf import settings
from django.core.management import call_command
from django.test import SimpleTestCase
from django.urls import reverse
from django.utils import translation

from scripts.check_stylesheet import classes, main

from .content import (
    PassageError,
    _expand_examples,
    _translate,
    coverage,
    missing_prose,
    untranslated,
)
from .nav import NAV, SLUGS
from .reference import attributes, cheat_sheet, table
from .views import BLOCK_EXTENDS


class PageRenderTests(SimpleTestCase):
    def test_every_page_renders(self):
        for code, _name in settings.LANGUAGES:
            with translation.override(code):
                urls = [
                    reverse("home"),
                    reverse("llms"),
                    reverse("llms-full"),
                ]
                for _section, pages in NAV:
                    for slug, _label in pages:
                        urls.append(
                            reverse("page", kwargs={"slug": slug})
                        )
                for name, page in block_pages():
                    urls.append(
                        reverse(
                            "block-preview", kwargs={"name": name, "page": page}
                        )
                    )

                for url in urls:
                    with self.subTest(url=url):
                        response = self.client.get(url)
                        self.assertEqual(response.status_code, 200)


def block_pages():
    """(block, page) for every page a block ships, found on disk."""
    return sorted(
        (path.parent.name, path.stem)
        for path in settings.COMPONENTS_DIR.glob("*/*.html")
        if path.read_text(encoding="utf-8").startswith(BLOCK_EXTENDS)
    )


class BlockPreviewTests(SimpleTestCase):
    def test_a_block_renders_inside_the_bare_frame(self):
        for name, page in block_pages():
            with self.subTest(block=name, page=page):
                response = self.client.get(
                    reverse("block-preview", kwargs={"name": name, "page": page})
                )
                self.assertTemplateUsed(response, "block_frame.html")
                self.assertTemplateNotUsed(response, "base.html")
                self.assertEqual(response["X-Frame-Options"], "SAMEORIGIN")

    def test_only_a_block_is_served(self):
        for name, page in [
            ("button", "index"),
            ("allauth", "login"),
            ("nothing", "page"),
        ]:
            with self.subTest(name=name):
                response = self.client.get(
                    reverse("block-preview", kwargs={"name": name, "page": page})
                )
                self.assertEqual(response.status_code, 404)


class StylesheetClassTests(SimpleTestCase):
    def test_reads_escaped_class_names(self):
        css = (
            ".hover\\:bg-accent:hover { margin: 0.5rem; }\n"
            ".w-1\\/2 { width: 50%; }\n"
            ".\\[\\&\\>svg\\]\\:size-4>svg { width: 1rem; }\n"
            ".\\32 xl\\:flex { display: flex; }\n"
            ".\\32 xl\\:grid { display: grid; }\n"
        )

        self.assertEqual(
            classes(css),
            {
                "hover\\:bg-accent",
                "w-1\\/2",
                "\\[\\&\\>svg\\]\\:size-4",
                "\\32 xl\\:flex",
                "\\32 xl\\:grid",
            },
        )


class StylesheetDiffTests(SimpleTestCase):
    def write(self, tmp_path, name, content):
        path = Path(tmp_path) / name
        path.write_bytes(content.encode("utf-8"))
        return str(path)

    def test_same_classes_different_declaration_fails(self):
        with tempfile.TemporaryDirectory() as tmp_path:
            committed = self.write(
                tmp_path, "committed.css", ".w-4 { width: 1rem; }\n"
            )
            build = self.write(
                tmp_path, "build.css", ".w-4 { width: 2rem; }\n"
            )

            with mock.patch.object(
                sys, "argv", ["check_stylesheet.py", committed, build]
            ):
                with self.assertRaises(SystemExit) as raised:
                    main()

            self.assertIn(
                "same classes, but the CSS differs", str(raised.exception)
            )

    def test_only_crlf_difference_passes(self):
        with tempfile.TemporaryDirectory() as tmp_path:
            committed = self.write(
                tmp_path, "committed.css", ".w-4 { width: 1rem; }\r\n"
            )
            build = self.write(
                tmp_path, "build.css", ".w-4 { width: 1rem; }\n"
            )

            with mock.patch.object(
                sys, "argv", ["check_stylesheet.py", committed, build]
            ):
                main()


DEMO = '<c-docs.demo-section>\n<c-button>Save</c-button>\n</c-docs.demo-section>\n'

PAGE = (
    DEMO
    + "\n:::en\n## Usage\n\nPress it.\n:::pt-br\n## Uso\n\nAperte.\n:::\n\n"
    + "```html\n<c-button>Save</c-button>\n```\n\n"
    + "Not translated yet.\n"
)


class PassageTests(SimpleTestCase):
    def test_the_active_language_picks_its_passage(self):
        body = _translate(PAGE, "pt-br")

        self.assertIn("## Uso\n\nAperte.", body)
        self.assertNotIn("Press it.", body)

    def test_a_missing_language_falls_back_to_english(self):
        body = _translate(PAGE, "es")

        self.assertIn("## Usage\n\nPress it.", body)
        self.assertIn("Not translated yet.", body)

    def test_the_demo_and_the_code_are_shared(self):
        for language in ("en", "pt-br", "es"):
            with self.subTest(language=language):
                body = _translate(PAGE, language)
                self.assertEqual(body.count("<c-button>Save</c-button>"), 2)
                self.assertNotIn(":::", body)

    def test_markers_inside_fenced_code_are_left_alone(self):
        body = "```text\n:::pt-br\n```\n"

        self.assertEqual(_translate(body, "pt-br"), body)

    def test_a_malformed_passage_is_refused(self):
        cases = {
            "fenced code": ":::en\n```html\n<p></p>\n```\n:::\n",
            "a demo": ":::en\n" + DEMO + ":::\n",
            "no English": ":::pt-br\nOlá.\n:::\n",
            "unknown language": ":::en\nHi.\n:::xx\nHi.\n:::\n",
            "a language twice": ":::en\nHi.\n:::en\nHi.\n:::\n",
            "never closed": ":::en\nHi.\n",
            "nothing to close": "Hi.\n:::\n",
        }

        for case, body in cases.items():
            with self.subTest(case=case):
                with self.assertRaises(PassageError):
                    _translate(body, "en")

    def test_untranslated_prose_is_reported_once_per_paragraph(self):
        self.assertEqual(missing_prose(PAGE, "pt-br"), ["Not translated yet."])
        self.assertEqual(
            missing_prose(PAGE, "es"), ["## Usage", "Not translated yet."]
        )

    def test_a_whole_file_override_counts_as_translated(self):
        self.assertEqual(untranslated("introduction", "pt-br"), [])
        self.assertEqual(untranslated("introduction", "en"), [])


class LlmsTxtTests(SimpleTestCase):
    def test_each_language_gets_its_own_summary_and_headings(self):
        expected = {
            "en": ("unofficial Django port", "## Optional"),
            "pt-br": ("port não oficial", "## Opcional"),
            "es": ("port no oficial", "## Opcional"),
        }

        for code, (summary, heading) in expected.items():
            with self.subTest(language=code), translation.override(code):
                index = self.client.get(reverse("llms")).content.decode()
                full = self.client.get(reverse("llms-full")).content.decode()

                self.assertIn(summary, index)
                self.assertIn(heading, index)
                self.assertIn(summary, full)


class TranslationCoverageTests(SimpleTestCase):
    def test_portuguese_is_complete(self):
        """M17 finished Portuguese; a page added without it fails here."""
        missing = coverage("pt-br")

        self.assertEqual(
            missing,
            {},
            "pages showing English in pt-br; add a :::pt-br passage and a "
            "description.pt-br:\n"
            + "\n".join(f"{slug}: {lines[0]}" for slug, lines in missing.items()),
        )

    def test_a_new_page_without_portuguese_is_reported(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root, "widget.md").write_text(
                "---\ntitle: Widget\ndescription: A widget.\n---\n\n"
                + DEMO
                + "\n## Usage\n\nPress it.\n",
                encoding="utf-8",
            )
            with mock.patch("docs.content.CONTENT_ROOT", Path(root)):
                missing = untranslated("widget", "pt-br")

        self.assertEqual(
            missing, ["description: A widget.", "## Usage", "Press it."]
        )

    def test_a_language_with_nothing_translated_reports(self):
        """A new language starts empty; the report lists every page and
        nothing fails."""
        missing = coverage("it")

        self.assertEqual(set(missing), set(SLUGS))

    def test_the_command_reports_every_language_but_english(self):
        output = io.StringIO()
        call_command("translation_coverage", stdout=output)

        self.assertIn("pt-br: ", output.getvalue())
        self.assertIn("es: ", output.getvalue())
        self.assertNotIn("en: ", output.getvalue())


class ExampleTests(SimpleTestCase):
    EXAMPLE = (
        '<c-docs.example class="min-h-[200px]">\n'
        "<div>\n"
        '  <a href="{% url \'page\' slug=\'button\' %}">Button</a>\n'
        "\n"
        "</div>\n"
        "</c-docs.example>\n"
    )

    def test_an_example_is_the_demo_and_its_own_source(self):
        body = _expand_examples(self.EXAMPLE)

        self.assertIn('<c-docs.demo-section class="min-h-[200px]">', body)
        self.assertIn(
            "```html\n<div>\n  <a href=\"{% url 'page' slug='button' %}\">"
            "Button</a>\n\n</div>\n```",
            body,
        )

    def test_the_demo_half_has_no_blank_line(self):
        demo = _expand_examples(self.EXAMPLE).split("```html")[0]

        self.assertNotIn("\n\n<", demo.strip())

    def test_the_code_shows_django_tags_unrendered(self):
        response = self.client.get(reverse("page", kwargs={"slug": "bubble"}))
        html = response.content.decode()

        # Rendered in the demo, written out in the code below it.
        self.assertRegex(html, r"\{% url (&#x27;|')page(&#x27;|') slug=")

    def test_no_demo_is_written_twice(self):
        """A demo followed by its own fenced copy is two sources of truth;
        <c-docs.example> makes it one."""
        pair = re.compile(
            r"</c-docs\.demo-section>\n\n+```html", re.MULTILINE
        )
        twice = [
            path.name
            for path in sorted((settings.BASE_DIR / "content").rglob("*.md"))
            if pair.search(path.read_text(encoding="utf-8"))
        ]

        self.assertEqual(twice, [], "write these demos with <c-docs.example>")


class ReferenceTests(SimpleTestCase):
    def test_every_row_is_an_attribute_the_template_declares(self):
        row = re.compile(r"^\| `<(c-[\w.-]+)>` \| `([\w-]+)` \|", re.MULTILINE)
        wrong = []

        for directory in sorted(settings.COMPONENTS_DIR.iterdir()):
            if not (directory / "index.html").is_file() and not any(
                directory.glob("*.html")
            ):
                continue
            for tag, name in row.findall(table(directory.name)):
                part = tag.split(".", 1)[1] if "." in tag else "index"
                source = (directory / f"{part.replace('-', '_')}.html").read_text(
                    encoding="utf-8"
                )
                declared = re.search(r"<c-vars\b([^>]*)>", source).group(1)
                if not re.search(rf"(^|\s){re.escape(name)}(=|\s|$)", declared):
                    wrong.append(f"{tag} {name}")

        self.assertEqual(wrong, [])

    def test_values_come_from_the_branches_and_include_the_default(self):
        source = (
            '<c-vars class="" size="md"></c-vars>'
            "{% if size == 'sm' %}a{% elif size == 'lg' %}b{% endif %}"
        )

        self.assertEqual(attributes(source), [("size", "md", ["md", "sm", "lg"])])

    def test_the_page_shows_the_table(self):
        response = self.client.get(reverse("page", kwargs={"slug": "button"}))

        self.assertContains(response, "<code>&lt;c-button&gt;</code>")
        self.assertContains(response, "<code>ghost</code>")


class CheatSheetTests(SimpleTestCase):
    def test_it_names_the_tag_the_parts_and_the_root_attributes(self):
        box = cheat_sheet("card", "<c-card>...</c-card>")

        self.assertIn("<code>&lt;c-card&gt;</code>", box)
        self.assertIn("<code>&lt;c-card.header&gt;</code>", box)
        self.assertTrue(box.endswith("```html\n<c-card>...</c-card>\n```"))

    def test_the_attributes_carry_their_defaults(self):
        box = cheat_sheet("button", "<c-button>Button</c-button>")

        self.assertIn("<code>variant=&quot;default&quot;</code>", box)
        self.assertNotIn("Parts", box)


# Component pages already rebuilt to the structure below. The last batch of
# the rebuild replaces this with every component page.
REBUILT = {
    "button",
    "a",
    "accordion",
    "alert",
    "alert-dialog",
    "aspect-ratio",
    "attachment",
    "avatar",
    "badge",
    "breadcrumb",
    "bubble",
    "button-group",
    "calendar",
    "card",
    "carousel",
    "chart",
    "checkbox",
    "code-block",
    "collapsible",
    "combobox",
    "command",
    "command-dialog",
    "context-menu",
    "date-picker",
    "dialog",
    "drawer",
    "dropdown-menu",
    "empty",
    "field",
    "form",
    "hover-card",
    "icon",
    "input",
    "input-group",
    "input-otp",
    "item",
    "kbd",
    "label",
    "marker",
    "menubar",
    "message",
    "message-scroller",
    "metric",
}


class PageStructureTests(SimpleTestCase):
    """A component page reads in one order: the demo, the cheat sheet,
    installation, usage, examples, RTL, accessibility, the API reference and
    notes. Examples and notes are the two a page may leave out."""

    ORDER = [
        ("demo", r"^<c-docs\.(?:demo-section|example)\b", True),
        ("cheat sheet", r"^<c-docs\.cheat-sheet ", True),
        ("installation", r"^## Installation$", True),
        ("usage", r"^## Usage$", True),
        ("examples", r"^## Examples$", False),
        ("rtl", r"^## RTL$", True),
        ("accessibility", r"^## Accessibility$", True),
        ("reference", r"^## API reference$", True),
        ("notes", r"^## Notes$", False),
    ]

    def test_rebuilt_pages_follow_the_order(self):
        wrong = []

        for slug in sorted(REBUILT):
            source = (settings.BASE_DIR / "content" / f"{slug}.md").read_text(
                encoding="utf-8"
            )
            english = _translate(source, "en")
            found = []
            for name, pattern, required in self.ORDER:
                match = re.search(pattern, english, re.MULTILINE)
                if match:
                    found.append((match.start(), name))
                elif required:
                    wrong.append(f"{slug}: no {name}")
            if [name for _at, name in sorted(found)] != [name for _at, name in found]:
                wrong.append(f"{slug}: sections out of order")

        self.assertEqual(wrong, [])
