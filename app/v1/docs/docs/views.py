from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render as render_page
from django.urls import reverse
from django.utils.translation import get_language_from_path, override
from django.views.decorators.clickjacking import xframe_options_sameorigin

from .content import PageNotFound
from .content import render as render_content
from .nav import NAV

ICONS_DIRECTORY = settings.COMPONENTS_DIR / "icon"

# What a block's page opens with, so it can extend another base when asked.
BLOCK_EXTENDS = '{% extends base_template|default:"base.html" %}'


def icon_names():
    """Whatever is in the icon directory, so the page cannot go stale."""
    return sorted(
        path.stem.replace("_", "-")
        for path in ICONS_DIRECTORY.glob("*.html")
        if path.stem != "index"
    )


# Pages whose examples come from data instead of being written out, because
# rendering from Django data is the point of the example.
PAGE_CONTEXT = {
    "icon": lambda: {"icons": icon_names()},
    "field": lambda: {
        "handle_errors": [
            "Handle is already taken.",
            "Handle must be lowercase.",
        ]
    },
    "native-select": lambda: {
        "countries": [
            ("br", "Brazil"),
            ("pt", "Portugal"),
            ("us", "United States"),
        ]
    },
}


def language_links(slug):
    """The current page in every language we publish."""
    links = []

    for code, name in settings.LANGUAGES:
        with override(code):
            links.append((code, name, reverse("page", kwargs={"slug": slug})))

    return links


def home(request):
    """The bare domain, honouring a language the visitor already picked.

    With prefix_default_language=False the unprefixed URLs *are* English, so
    Django ignores the language cookie there on purpose. That is right for
    every page but the entry point, where someone arriving without a prefix
    should land in the language they chose last time.
    """
    chosen = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)
    unprefixed = get_language_from_path(request.path_info) is None

    if (
        unprefixed
        and chosen != settings.LANGUAGE_CODE
        and chosen in dict(settings.LANGUAGES)
    ):
        with override(chosen):
            return redirect("home")

    return page(request, slug="introduction")


def page(request, slug):
    try:
        meta, content = render_content(slug, PAGE_CONTEXT.get(slug, dict)())
    except PageNotFound:
        raise Http404(slug) from None

    return render_page(
        request,
        "page.html",
        {
            "meta": meta,
            "content": content,
            "nav": NAV,
            "slug": slug,
            "languages": language_links(slug),
        },
    )


# The portal frames it, and only the portal: same origin, never DENY.
@xframe_options_sameorigin
def block_preview(request, name, page):
    """A block's page as the CLI installs it, inside a bare frame.

    The page extends `base_template` when it is given, so the preview passes
    a frame with the stylesheet and Alpine in place of a project's base.html.
    Only files that open that way are served: anything else is not a block.
    """
    directory = name.replace("-", "_")
    path = settings.COMPONENTS_DIR / directory / f"{page}.html"

    if not path.is_file() or not path.read_text(encoding="utf-8").startswith(
        BLOCK_EXTENDS
    ):
        raise Http404(name)

    return render_page(
        request,
        f"{settings.COMPONENTS_DIR.name}/{directory}/{page}.html",
        {"base_template": "block_frame.html"},
    )
