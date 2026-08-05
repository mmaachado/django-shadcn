"""Every component has to survive being rendered by cotton itself.

Compiling a template proves its Django syntax; it says nothing about how
cotton parses the component tag. That gap let a {{ attrs }} broken across a
line ship, because Django substitutes it and cotton does not.
"""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

import django
import pytest
from django.conf import settings

REPO_ROOT = Path(__file__).resolve().parent.parent
COMPONENTS_ROOT = REPO_ROOT / 'components'

if not settings.configured:
    settings.configure(
        DEBUG=True,
        INSTALLED_APPS=['django_cotton'],
        COTTON_DIR='components',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                # The repository root stands in for the user's project, where
                # the components land under templates/cotton/.
                'DIRS': [REPO_ROOT],
                'APP_DIRS': True,
                'OPTIONS': {'builtins': ['django_cotton.templatetags.cotton']},
            }
        ],
        USE_TZ=True,
    )
    django.setup()

# allauth ships page templates rather than cotton components, and they open
# with {% load account %} from a library we do not install.
NOT_COMPONENTS = {'allauth'}

# Required attributes, so the component has something to render.
CONTEXT = {
    'icon': {'name': 'check'},
    'icon.index': {'name': 'check'},
}


def tag_for(template: Path) -> str:
    """The cotton tag that renders this file."""
    relative = template.relative_to(COMPONENTS_ROOT).with_suffix('')
    parts = list(relative.parts)
    if parts[-1] == 'index':
        parts.pop()
    return '.'.join(part.replace('_', '-') for part in parts)


def component_tags() -> list[str]:
    tags = []
    for template in sorted(COMPONENTS_ROOT.rglob('*.html')):
        if template.relative_to(COMPONENTS_ROOT).parts[0] in NOT_COMPONENTS:
            continue
        tags.append(tag_for(template))
    return tags


PROBE = 'probe-class'


def render(tag: str, **extra: str) -> str:
    """Render a component the way a page does.

    The compiler is what turns <c-name> into the tag that loads the
    component; Django's engine on its own hands the markup straight back.
    """
    from django.template import Context, Template
    from django_cotton.compiler_regex import CottonCompiler

    attributes = ' '.join(
        f'{name}="{value}"'
        for name, value in (CONTEXT.get(tag, {}) | extra).items()
    )
    source = f'<c-{tag} {attributes}>slot</c-{tag}>'

    return Template(CottonCompiler().process(source)).render(Context({}))


class Tags(HTMLParser):
    """Collects every start tag with the attribute names it carries."""

    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, [name for name, _ in attrs]))

    handle_startendtag = handle_starttag


@pytest.mark.parametrize('tag', component_tags())
def test_component_renders_through_cotton(tag):
    rendered = render(tag)

    assert rendered.strip(), f'<c-{tag}> rendered nothing'
    leftovers = [piece for piece in ('{{', '{%') if piece in rendered]
    assert not leftovers, (
        f'<c-{tag}> left template syntax in its output: {rendered.strip()}'
    )


@pytest.mark.parametrize('tag', component_tags())
def test_no_element_carries_the_same_attribute_twice(tag):
    """cotton leaves class inside attrs unless the component declares it.

    A component writing both {{ class }} and {{ attrs }} then emits class
    twice. The parser keeps whichever comes first, so the one the component
    wrote can be the one thrown away.
    """
    parser = Tags()
    parser.feed(render(tag, **{'class': PROBE}))

    repeated = []
    for name, attrs in parser.tags:
        twice = sorted(k for k, n in Counter(attrs).items() if n > 1)
        if twice:
            repeated.append(f'<{name}> repeats {twice}')

    assert not repeated, f'<c-{tag}>: ' + '; '.join(repeated)


@pytest.mark.parametrize('tag', component_tags())
def test_the_class_lands_on_one_element(tag):
    parser = Tags()
    rendered = render(tag, **{'class': PROBE})
    parser.feed(rendered)

    if not any('class' in attrs for _, attrs in parser.tags):
        pytest.skip(f'<c-{tag}> renders no element carrying a class')

    assert rendered.count(PROBE) == 1, (
        f'<c-{tag}> put the class on {rendered.count(PROBE)} elements'
    )


def test_the_component_tag_is_really_being_processed():
    """Guards the check above against passing on unprocessed markup."""
    assert '<c-button' not in render('button')
