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
