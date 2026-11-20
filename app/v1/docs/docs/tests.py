"""Request every public page of the portal, in every language.

A template error in content/, a broken nav.py entry or a missing static
manifest would otherwise only show up after the deploy. Run collectstatic
first: the storage backend raises when the manifest is missing.
"""

import sys
import tempfile
from pathlib import Path
from unittest import mock

from django.conf import settings
from django.test import SimpleTestCase
from django.urls import reverse
from django.utils import translation

from scripts.check_stylesheet import classes, main

from .content import (
    PassageError,
    _translate,
    missing_prose,
    untranslated,
)
from .nav import NAV


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

                for url in urls:
                    with self.subTest(url=url):
                        response = self.client.get(url)
                        self.assertEqual(response.status_code, 200)


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
