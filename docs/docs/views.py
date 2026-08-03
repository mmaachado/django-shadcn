from django.conf import settings
from django.shortcuts import render

ICONS_DIRECTORY = settings.BASE_DIR.parent / "components" / "icon"

# Django tags inside a display_code string would be picked up by the template
# lexer, so this one comes in through the context instead.
CHOICES_SNIPPET = """<c-native-select name="country">
    {% for value, label in form.country.field.choices %}
        <c-native-select.option value="{{ value }}">{{ label }}</c-native-select.option>
    {% endfor %}
</c-native-select>"""


def introduction(request):
    return render(request, "introduction.html")


def installation(request):
    return render(request, "installation.html")


def accordion(request):
    return render(request, "accordion.html")


def alert(request):
    return render(request, "alert.html")


def alert_dialog(request):
    return render(request, "alert_dialog.html")


def aspect_ratio(request):
    return render(request, "aspect_ratio.html")


def avatar(request):
    return render(request, "avatar.html")


def badge(request):
    return render(request, "badge.html")


def breadcrumb(request):
    return render(request, "breadcrumb.html")


def button(request):
    return render(request, "button.html")


def button_group(request):
    return render(request, "button_group.html")


def card(request):
    return render(request, "card.html")


def checkbox(request):
    return render(request, "checkbox.html")


def combobox(request):
    return render(request, "combobox.html")


def command(request):
    return render(request, "command.html")


def command_dialog(request):
    return render(request, "command_dialog.html")


def dialog(request):
    return render(request, "dialog.html")


def dropdown_menu(request):
    return render(request, "dropdown_menu.html")


def empty(request):
    return render(request, "empty.html")


def field(request):
    handle_errors = ["Handle is already taken.", "Handle must be lowercase."]
    return render(request, "field.html", {"handle_errors": handle_errors})


def form(request):
    return render(request, "form.html")


def icon(request):
    """Lists whatever is in the icon directory, so the page cannot go stale."""
    names = sorted(
        path.stem.replace("_", "-")
        for path in ICONS_DIRECTORY.glob("*.html")
        if path.stem != "index"
    )
    return render(request, "icon.html", {"icons": names})


def input(request):
    return render(request, "input.html")


def input_group(request):
    return render(request, "input_group.html")


def item(request):
    return render(request, "item.html")


def kbd(request):
    return render(request, "kbd.html")


def label(request):
    return render(request, "label.html")


def native_select(request):
    countries = [
        ("br", "Brazil"),
        ("pt", "Portugal"),
        ("us", "United States"),
    ]
    return render(
        request,
        "native_select.html",
        {"countries": countries, "choices_snippet": CHOICES_SNIPPET},
    )


def navigation_menu(request):
    return render(request, "navigation_menu.html")


def popover(request):
    return render(request, "popover.html")


def progress(request):
    return render(request, "progress.html")


def select(request):
    return render(request, "select.html")


def separator(request):
    return render(request, "separator.html")


def skeleton(request):
    return render(request, "skeleton.html")


def spinner(request):
    return render(request, "spinner.html")


def sheet(request):
    sides = ["top", "right", "bottom", "left"]
    return render(request, "sheet.html", {"sides": sides})


def table(request):
    return render(request, "table.html")


def tabs(request):
    return render(request, "tabs.html")


def textarea(request):
    return render(request, "textarea.html")


def typography(request):
    return render(request, "typography.html")


def toast(request):
    return render(request, "toast.html")


def allauth(request):
    return render(request, "allauth.html")
