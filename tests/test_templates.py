"""Every shipped template has to be valid Django template syntax.

A malformed {% if %} only shows up when a user renders the component in
their own project, which is the worst place to find out.
"""

import re

import pytest
from django.template import Engine
from django.template.exceptions import TemplateSyntaxError

engine = Engine(
    libraries={
        'i18n': 'django.templatetags.i18n',
        'account': 'tests.templatetags_stub',
    }
)


def test_components_are_discovered(component_templates):
    assert component_templates, 'no component templates found'


def test_templates_compile(component_templates):
    errors = []

    for template in component_templates:
        source = template.read_text(encoding='utf-8')
        try:
            engine.from_string(source)
        except TemplateSyntaxError as error:
            errors.append(f'{template.name}: {error}')

    assert not errors, 'invalid templates:\n' + '\n'.join(errors)


@pytest.mark.parametrize('unbalanced', ['{% if x %}', '{% for x in y %}'])
def test_compilation_catches_unclosed_tags(unbalanced):
    """Guards the check above against silently passing everything."""
    with pytest.raises(TemplateSyntaxError):
        engine.from_string(unbalanced)


# x-data="{ v: '{{ value }}' }" looks escaped, but Django escapes for HTML and
# the browser decodes the entities back before Alpine evaluates the attribute
# as JavaScript. A value carrying a quote closes the literal and whatever
# follows runs. Values reach Alpine through data-* instead.
ALPINE_ATTRIBUTE = re.compile(
    r'(?:x-[a-z:.\-]+|@[a-z:.\-]+|:[a-z\-]+)\s*=\s*"([^"]*)"'
)


def test_no_template_value_lands_inside_an_alpine_expression(
    component_templates,
):
    offenders = []

    for template in component_templates:
        source = template.read_text(encoding='utf-8')
        for expression in ALPINE_ATTRIBUTE.findall(source):
            if '{{' in expression:
                offenders.append(f'{template.parent.name}/{template.name}')
                break

    assert not offenders, (
        'template values interpolated into Alpine expressions: '
        f'{sorted(set(offenders))}'
    )


# An editor that reflows a long attribute list can land the newline inside
# {{ attrs }}. Django still substitutes it; cotton 2.x does not, and the
# braces reach the page as text.
INTERPOLATION = re.compile(r'\{\{[^{}]*\}\}', re.DOTALL)


def test_interpolations_stay_on_one_line(component_templates):
    offenders = []

    for template in component_templates:
        source = template.read_text(encoding='utf-8')
        for match in INTERPOLATION.finditer(source):
            if '\n' in match.group(0):
                name = f'{template.parent.name}/{template.name}'
                offenders.append(f'{name}: {match.group(0)!r}')

    assert not offenders, 'interpolations split across lines:\n' + '\n'.join(
        offenders
    )


def test_the_message_scroller_stays_hidden_until_it_opens(components_root):
    """A transcript opened at the end used to paint its oldest rows first.

    The viewport renders pending and Alpine clears the flag once the opening
    position applies. The rule only hides it with scripting on, so a page
    without JavaScript, which nothing would ever clear, still shows the rows.
    """
    viewport = (
        components_root / 'message_scroller' / 'viewport.html'
    ).read_text(encoding='utf-8')

    assert 'data-pending-scroll="true"' in viewport
    assert (
        "x-bind:data-pending-scroll=\"opened ? 'false' : 'true'\"" in viewport
    )
    assert (
        '[@media(scripting:enabled)]:data-[pending-scroll=true]:invisible'
        in viewport
    )


def test_tabs_report_the_selected_tab_and_take_the_arrow_keys(
    components_root,
):
    """A screen reader could not tell which tab was open, nor which panel
    belonged to which tab, and only Tab moved between them."""

    def read(name):
        return (components_root / 'tabs' / name).read_text(encoding='utf-8')

    root, trigger, panel = (
        read('index.html'),
        read('trigger.html'),
        read('content.html'),
    )

    assert "x-id=\"['tab', 'tabpanel']\"" in root
    assert 'x-bind:aria-selected="(activeTab === own).toString()"' in trigger
    assert 'x-bind:id="$id(\'tab\', own)"' in trigger
    assert 'x-bind:aria-controls="$id(\'tabpanel\', own)"' in trigger
    assert 'x-bind:tabindex="reachable($el) ? 0 : -1"' in trigger
    assert 'x-bind:id="$id(\'tabpanel\', own)"' in panel
    assert 'x-bind:aria-labelledby="$id(\'tab\', own)"' in panel
    assert '@keydown="move($event)"' in read('list.html')
    assert "direction === 'rtl'" in root


def test_the_select_is_a_combobox_the_keyboard_can_choose_from(
    components_root,
):
    """The options were divs nothing could reach: a keyboard opened the
    list and could only close it again."""

    def read(name):
        return (components_root / 'select' / name).read_text(encoding='utf-8')

    root, trigger, item = (
        read('index.html'),
        read('trigger.html'),
        read('item.html'),
    )

    assert '@keydown="key($event)"' in trigger
    assert 'role="combobox"' in trigger
    assert 'aria-haspopup="listbox"' in trigger
    assert 'x-bind:aria-activedescendant=' in trigger
    assert 'x-bind:id="$id(\'select-listbox\')"' in read('content.html')
    assert 'x-bind:id="$id(\'select-option\', own)"' in item
    assert 'x-bind:aria-selected="(value === own).toString()"' in item
    for key in ('ArrowDown', 'ArrowUp', 'Home', 'End', 'Enter', 'Tab'):
        assert f"'{key}'" in root
    assert ':not([data-disabled])' in root


MODALS = (
    'dialog/content.html',
    'alert_dialog/content.html',
    'sheet/content.html',
    'drawer/content.html',
    'command_dialog/index.html',
)
FOCUS_IN_AND_BACK = re.compile(r'x-init="let back = null;[^"]*"')
FOCUS_TRAP = re.compile(
    r"@keydown\.window=\"if \(open && \$event\.key === 'Tab'\)[^\"]*\""
)


def test_every_modal_keeps_focus_inside_and_gives_it_back(components_root):
    """Tab walked out of an open dialog into the page behind it, and closing
    one left focus wherever it fell. The five modals carry the same trap,
    so a fix to one has to reach them all."""
    found = {}

    for name in MODALS:
        source = (components_root / name).read_text(encoding='utf-8')
        opened = FOCUS_IN_AND_BACK.findall(source)
        trapped = FOCUS_TRAP.findall(source)
        assert len(opened) == len(trapped) == 1, name
        assert 'role="dialog"' in source and 'aria-modal="true"' in source
        found[name] = (opened[0], trapped[0])

    assert len(set(found.values())) == 1, 'the modals trap focus differently'
    opened, trapped = next(iter(found.values()))
    assert 'back.focus()' in opened
    assert '$event.shiftKey' in trapped


MENUS = ('dropdown_menu', 'context_menu', 'menubar')
MENU_KEYS = re.compile(
    r'@keydown="const items = \[\.\.\.\$el\.querySelectorAll[^"]*"'
)
SUB_KEYS = re.compile(
    r'@keydown="if \(\$event\.key === \(getComputedStyle[^"]*"'
)


def test_every_menu_takes_the_arrow_keys(components_root):
    """The items were divs nothing could focus: an open menu answered to the
    pointer and to Escape, and the keyboard could not reach anything in it.
    Every panel, top level or submenu, carries the same handler."""
    panels, subs = set(), set()

    for menu in MENUS:

        def read(name, menu=menu):
            path = components_root / menu / f'{name}.html'
            return path.read_text(encoding='utf-8')

        for name in ('content', 'sub_content'):
            found = MENU_KEYS.findall(read(name))
            assert len(found) == 1, f'{menu}/{name}'
            panels.add(found[0])
        for name in ('item', 'checkbox_item', 'radio_item', 'sub_trigger'):
            assert 'tabindex="-1"' in read(name), f'{menu}/{name}'
        found = SUB_KEYS.findall(read('sub_trigger'))
        assert len(found) == 1, f'{menu}/sub_trigger'
        subs.add(found[0])
        assert 'rtl:rotate-180' in read('sub_trigger')
        assert '@focusout=' in read('content')

    assert len(panels) == 1, 'the menus handle keys differently'
    assert len(subs) == 1, 'the submenu triggers handle keys differently'
    (keys,) = panels
    for key in ('ArrowDown', 'ArrowUp', 'Home', 'End', 'Enter', 'subOpen'):
        assert key in keys
    assert "direction === 'rtl'" in keys


def test_the_menubar_moves_between_its_menus(components_root):
    source = (components_root / 'menubar' / 'index.html').read_text(
        encoding='utf-8'
    )
    assert "querySelectorAll('[data-slot=menubar-trigger]" in source
    assert "direction === 'rtl' ? 'ArrowLeft' : 'ArrowRight'" in source


# A name declared in <c-vars> and never read does nothing, yet the docs'
# generated reference lists it as an attribute. The ones below are declared on
# purpose: declaring a name keeps cotton from writing it onto the element.
CVARS = re.compile(r'<c-vars\b(.*?)/?>(?:</c-vars>)?', re.DOTALL)
DECLARED = re.compile(r'(?<![\w-]):?([a-zA-Z_][\w-]*)(?:="[^"]*")?')
SWALLOWED = {
    ('accordion/item.html', 'value'): (
        'the item shares its value with its trigger and content, and only '
        'they read it; on the item it would land on the <div>'
    ),
}


def test_every_declared_attribute_is_read(
    component_templates, components_root
):
    unread = []

    for template in component_templates:
        source = template.read_text(encoding='utf-8')
        declaration = CVARS.search(source)
        if declaration is None:
            continue
        body = source[: declaration.start()] + source[declaration.end() :]
        path = template.relative_to(components_root).as_posix()
        for name in DECLARED.findall(declaration.group(1)):
            if name == 'class' or (path, name) in SWALLOWED:
                continue
            if not re.search(rf'(?<![\w-]){re.escape(name)}(?![\w-])', body):
                unread.append(f'{path}: {name}')

    assert not unread, 'declared but never read:\n' + '\n'.join(unread)
