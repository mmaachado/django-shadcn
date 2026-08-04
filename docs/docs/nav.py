"""The sidebar, and the order the docs are listed in.

Every entry is a slug under content/ and a label. Adding a page means adding a
line here; there is no route or view to write.
"""

from django.utils.translation import gettext_lazy as _

NAV = [
    (
        _("Getting Started"),
        [
            ("introduction", _("Introduction")),
            ("installation", _("Installation")),
        ],
    ),
    (
        _("Blocks"),
        [
            ("allauth", "django-allauth"),
        ],
    ),
    (
        _("Components"),
        [
            ("accordion", "Accordion"),
            ("alert", "Alert"),
            ("alert-dialog", "Alert Dialog"),
            ("aspect-ratio", "Aspect Ratio"),
            ("avatar", "Avatar"),
            ("badge", "Badge"),
            ("breadcrumb", "Breadcrumb"),
            ("button", "Button"),
            ("button-group", "Button Group"),
            ("card", "Card"),
            ("checkbox", "Checkbox"),
            ("combobox", "Combobox"),
            ("command", "Command"),
            ("command-dialog", "Command Dialog"),
            ("dialog", "Dialog"),
            ("dropdown-menu", "Dropdown Menu"),
            ("empty", "Empty"),
            ("field", "Field"),
            ("form", "Form"),
            ("icon", "Icon"),
            ("input", "Input"),
            ("input-group", "Input Group"),
            ("item", "Item"),
            ("kbd", "Kbd"),
            ("label", "Label"),
            ("native-select", "Native Select"),
            ("navigation-menu", "Navigation Menu"),
            ("popover", "Popover"),
            ("progress", "Progress"),
            ("select", "Select"),
            ("separator", "Separator"),
            ("sheet", "Sheet"),
            ("skeleton", "Skeleton"),
            ("spinner", "Spinner"),
            ("table", "Table"),
            ("tabs", "Tabs"),
            ("textarea", "Textarea"),
            ("toast", "Toast"),
            ("typography", "Typography"),
        ],
    ),
]

SLUGS = [slug for _, entries in NAV for slug, _ in entries]
