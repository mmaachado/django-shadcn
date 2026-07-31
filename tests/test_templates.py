"""Every shipped template has to be valid Django template syntax.

A malformed {% if %} only shows up when a user renders the component in
their own project, which is the worst place to find out.
"""

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
