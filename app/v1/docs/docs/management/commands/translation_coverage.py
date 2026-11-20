"""Report, per language, the pages that still show English.

Portuguese is complete and a test keeps it that way. The other languages are
partial on purpose, and this is what keeps them visible:

    uv run python manage.py translation_coverage
    uv run python manage.py translation_coverage --language es --verbose
"""

from django.conf import settings
from django.core.management.base import BaseCommand

from docs.content import coverage
from docs.nav import SLUGS


class Command(BaseCommand):
    help = "List the pages that still show English, per language."

    def add_arguments(self, parser):
        parser.add_argument(
            "--language",
            action="append",
            help="a language code; repeat for several, or leave out for all",
        )
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="also print the first English line of each missing passage",
        )

    def handle(self, *args, **options):
        languages = options["language"] or [
            code for code, _name in settings.LANGUAGES if code != "en"
        ]

        for language in languages:
            report = coverage(language)
            done = len(SLUGS) - len(report)
            self.stdout.write(
                f"{language}: {done}/{len(SLUGS)} pages translated, "
                f"{len(report)} still in English"
            )
            for slug, missing in report.items():
                self.stdout.write(f"  {slug} ({len(missing)})")
                if options["verbose"]:
                    for line in missing:
                        self.stdout.write(f"    {line}")
