from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render as render_page
from django.urls import reverse
from django.utils.translation import get_language_from_path, override

from .content import PageNotFound
from .content import render as render_content
from .nav import NAV

ICONS_DIRECTORY = settings.BASE_DIR.parent / "components" / "icon"


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
