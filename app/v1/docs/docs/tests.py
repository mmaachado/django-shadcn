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
