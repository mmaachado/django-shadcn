"""Components use logical utilities, so they mirror under dir="rtl".

ms-/me-/ps-/pe-, start-/end-, text-start/text-end, border-s/border-e and
rounded-s/rounded-e follow the direction of the text. Their physical
counterparts do not, and neither does translate-x, which has no logical form
and needs an rtl: twin with the opposite sign (space-x is fine: Tailwind v4
compiles it to margin-inline). A new component that uses one looks right in
English and wrong in Arabic, with nothing failing. The few physical
utilities that are meant are listed below, each with the reason.
"""

import re

import pytest

COMMENT = re.compile(r'{% comment %}.*?{% endcomment %}', re.DOTALL)

# Whitespace and quotes end a class, and so do template tags, which sit flush
# against classes in {% if %}left-0{% endif %}.
TOKEN_BOUNDARY = re.compile(r"""[\s"'`]+|{%|%}|{{|}}|[{}]""")

PHYSICAL = re.compile(
    r'^-?(?:scroll-)?[mp][lr]-'
    r'|^-?(?:left|right)-'
    r'|^-?translate-x-(?!0$)'
    r'|^text-(?:left|right)$'
    r'|^border-[lr](?:-|$)'
    r'|^rounded-(?:[lr]|[tb][lr])(?:-|$)'
    r'|^(?:float|clear)-(?:left|right)$'
    r'|^origin-(?:.+-)?(?:left|right)$'
)

SIDE = (
    'the side prop names a side of the screen, which does not change with '
    'the direction'
)
CENTRE = (
    'left-1/2 with -translate-x-1/2 centres the element, and the centre does '
    'not move with the direction'
)

# Path under components/ -> (physical utilities allowed there, why).
EXCEPTIONS = {
    'carousel/next.html': (
        {'-right-12', 'left-1/2', '-translate-x-1/2'},
        'the carousel scrolls in physical coordinates, with scrollLeft and '
        'the arrow keys, so its buttons keep their sides',
    ),
    'carousel/previous.html': (
        {'-left-12', 'left-1/2', '-translate-x-1/2'},
        'the carousel scrolls in physical coordinates, with scrollLeft and '
        'the arrow keys, so its buttons keep their sides',
    ),
    'chart/axis_x.html': (
        {'-translate-x-1/2'},
        'each label is centred on the x its style sets, and the plot does not '
        'mirror',
    ),
    'chart/line.html': (
        {'-translate-x-1/2'},
        'each dot is centred on the x its style sets, and the plot does not '
        'mirror',
    ),
    'chart/axis_y.html': (
        {'left-0', 'pr-2', 'text-right'},
        'the value axis is part of the plot, which does not mirror',
    ),
    'command_dialog/index.html': (
        {'left-[50%]', 'translate-x-[-50%]'},
        CENTRE,
    ),
    'dropdown_menu/content.html': ({'left-1/2', '-translate-x-1/2'}, CENTRE),
    'menubar/content.html': ({'left-1/2', '-translate-x-1/2'}, CENTRE),
    'message_scroller/button.html': ({'left-1/2', '-translate-x-1/2'}, CENTRE),
    'resizable/handle.html': (
        {'left-0', 'left-1/2', '-translate-x-1/2'},
        'the hit area is centred on the line or stretched across it, which '
        'is the same in either direction',
    ),
    'drawer/content.html': (
        {
            'left-0',
            'right-0',
            'border-l',
            'border-r',
            'translate-x-full',
            '-translate-x-full',
        },
        'direction="left" and direction="right" name a side of the screen',
    ),
    'sheet/content.html': (
        {'left-0', 'right-0', 'translate-x-full', '-translate-x-full'},
        SIDE,
    ),
    'sidebar/index.html': (
        {
            'left-0',
            'right-0',
            'left-[calc(var(--sidebar-width)*-1)]',
            'right-[calc(var(--sidebar-width)*-1)]',
            'border-l',
            'border-r',
            'translate-x-full',
            '-translate-x-full',
        },
        SIDE,
    ),
    'sidebar/rail.html': (
        {
            '-left-2',
            '-right-2',
            '-right-4',
            'left-0',
            'left-1/2',
            'left-full',
            '-translate-x-1/2',
        },
        'the rail sits on the edge of the sidebar, and ' + SIDE,
    ),
    'tooltip/content.html': (
        {
            'left-full',
            'right-full',
            'ml-1.5',
            'mr-1.5',
            'left-1/2',
            '-translate-x-1/2',
        },
        f'{SIDE}; {CENTRE}',
    ),
    'hover_card/content.html': (
        {
            'left-full',
            'right-full',
            'ml-1',
            'mr-1',
            'left-1/2',
            '-translate-x-1/2',
        },
        f'{SIDE}; {CENTRE}',
    ),
}


def utility(token: str) -> str:
    """The utility without its variants: what follows the last colon that
    is not inside brackets, so [&>svg]:left-4 gives left-4."""
    depth = start = 0
    for at, char in enumerate(token):
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char == ':' and depth == 0:
            start = at + 1
    return token[start:]


def mirrored(token: str, tokens: set[str]) -> bool:
    """A translate-x that is the rtl: twin, or has one: the same variants
    under rtl:, with the opposite sign."""
    bare = utility(token)
    if not bare.lstrip('-').startswith('translate-x-'):
        return False
    variants = token[: len(token) - len(bare)]
    if variants.startswith('rtl:'):
        return True
    opposite = bare[1:] if bare.startswith('-') else f'-{bare}'
    return f'rtl:{variants}{opposite}' in tokens


def physical_utilities(source: str) -> set[str]:
    """Physical direction utilities in a template, comments excluded:
    the comments that explain an exception name the utility."""
    tokens = set(TOKEN_BOUNDARY.split(COMMENT.sub('', source)))
    return {
        utility(token)
        for token in tokens
        if PHYSICAL.search(utility(token)) and not mirrored(token, tokens)
    }


def relative(template, components_root) -> str:
    return template.relative_to(components_root).as_posix()


def test_no_physical_direction_utility(component_templates, components_root):
    offenders = []

    for template in component_templates:
        name = relative(template, components_root)
        allowed = EXCEPTIONS.get(name, (set(), ''))[0]
        found = physical_utilities(template.read_text(encoding='utf-8'))
        if found - allowed:
            offenders.append(f'{name}: {", ".join(sorted(found - allowed))}')

    assert not offenders, (
        'physical utilities that do not mirror under dir="rtl"; use '
        'ms-/me-/ps-/pe-, start-/end-, text-start/text-end, border-s/border-e '
        'or rounded-s/rounded-e, or add the file to EXCEPTIONS with the '
        'reason:\n' + '\n'.join(offenders)
    )


def test_every_exception_is_still_used(components_root):
    """An exception the template no longer needs would let the utility back
    in unnoticed."""
    stale = []

    for name, (allowed, _) in EXCEPTIONS.items():
        source = (components_root / name).read_text(encoding='utf-8')
        if allowed - physical_utilities(source):
            unused = ', '.join(sorted(allowed - physical_utilities(source)))
            stale.append(f'{name}: {unused}')

    assert not stale, 'exceptions no longer in the template:\n' + '\n'.join(
        stale
    )


def test_every_exception_says_why():
    assert all(reason for _, reason in EXCEPTIONS.values())


def test_ml_2_in_any_component_is_caught(component_templates):
    """Guards the scan against silently passing everything: ml-2 added to
    the first class attribute of every template is found."""
    missed = []

    for template in component_templates:
        source = template.read_text(encoding='utf-8')
        if 'class="' not in source:
            continue
        if 'ml-2' not in physical_utilities(
            source.replace('class="', 'class="ml-2 ', 1)
        ):
            missed.append(template.name)

    assert not missed, 'ml-2 not found in:\n' + '\n'.join(missed)


@pytest.mark.parametrize(
    'source, expected',
    [
        ('<div class="ml-2">', 'ml-2'),
        ('<div class="-mr-4">', '-mr-4'),
        ('<div class="hover:pl-8">', 'pl-8'),
        ('<div class="[&>svg]:left-4">', 'left-4'),
        ('<div class="data-[inset=true]:pr-2">', 'pr-2'),
        ('{% if side %}right-0{% endif %}', 'right-0'),
        ('<td class="text-right">', 'text-right'),
        ('<span class="first:border-l">', 'border-l'),
        ('<span class="rounded-tr-md">', 'rounded-tr-md'),
        ('x-bind:class="{ \'text-left\': on }"', 'text-left'),
        ('<img class="float-left">', 'float-left'),
        ('<span class="translate-x-full">', 'translate-x-full'),
        ('<span class="checked:-translate-x-px">', '-translate-x-px'),
        (
            '<span class="checked:translate-x-4 rtl:translate-x-4">',
            'translate-x-4',
        ),
    ],
)
def test_physical_utility_is_found(source, expected):
    assert physical_utilities(source) == {expected}


@pytest.mark.parametrize(
    'source',
    [
        '<div class="ms-2 me-2 ps-4 pe-4 start-0 end-0">',
        '<div class="text-start text-end border-s rounded-e-md">',
        '<div class="rounded-lg border-ring place-items-center">',
        '<div class="data-[side=left]:ms-1">',
        '<div x-on:keydown.left.prevent="previous()">',
        "<div x-bind:style=\"'left: ' + offset + 'px'\">",
        '{% comment %}pr-2 stays physical{% endcomment %}',
        '<div class="translate-x-0 space-x-2 -space-x-1 translate-y-full">',
        '<span class="translate-x-full rtl:-translate-x-full">',
        '<span class="checked:-translate-x-px rtl:checked:translate-x-px">',
    ],
)
def test_logical_utility_and_lookalike_pass(source):
    assert physical_utilities(source) == set()
