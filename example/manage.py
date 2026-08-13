"""A Django project small enough to read, for looking at a component.

It renders `templates/index.html` against the components in this checkout
rather than a copy of them, so editing one and reloading is the whole loop.

    uv run python example/manage.py runserver
"""

import json
import sys
from pathlib import Path

import django
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent

settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=['*'],
    # Nothing here is served anywhere; the project has no database and no
    # session, so there is nothing for a key to protect.
    SECRET_KEY='django-shadcn-example',
    ROOT_URLCONF=__name__,
    # SimpleAppConfig rather than 'django_cotton': the default one wraps every
    # loader in Django's cached.Loader, which keys compiled templates by name
    # and never looks at the file again. In a server that stays up, that means
    # editing a component changes nothing until the process restarts — which
    # is the opposite of what this project is for. The loaders below are the
    # same ones, without that wrapper.
    INSTALLED_APPS=[
        'django.contrib.staticfiles',
        'django_cotton.apps.SimpleAppConfig',
    ],
    # <c-button> resolves to <a template dir>/components/button/index.html,
    # which is the library itself.
    COTTON_DIR='components',
    STATIC_URL='static/',
    STATICFILES_DIRS=[HERE / 'static'],
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [REPO_ROOT, HERE / 'templates'],
            'OPTIONS': {
                'builtins': ['django_cotton.templatetags.cotton'],
                'loaders': [
                    'django_cotton.cotton_loader.Loader',
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ],
            },
        }
    ],
    USE_TZ=True,
)


def submitted(request):
    """Echo a posted form, for the components that are one.

    There is no middleware, so no CSRF token to carry — this project never
    leaves the machine it runs on.
    """
    return JsonResponse(dict(request.POST.lists()))


def index(request):
    """Whatever the component being worked on needs.

    A chart takes its data as JSON, so it is serialised here rather than
    written into the template: a string literal in a template is already safe
    as far as Django is concerned, and the quotes would reach the attribute
    unescaped and cut it short.
    """
    return render(
        request,
        'index.html',
        {
            'series': json.dumps(
                [
                    {'month': 'Jan', 'revenue': 1200, 'profit': 300},
                    {'month': 'Feb', 'revenue': 1800, 'profit': 500},
                    {'month': 'Mar', 'revenue': 1500, 'profit': 400},
                    {'month': 'Apr', 'revenue': 2400, 'profit': 900},
                    {'month': 'May', 'revenue': 2100, 'profit': 700},
                    {'month': 'Jun', 'revenue': 3000, 'profit': 1100},
                ]
            ),
            'config': json.dumps(
                {
                    'revenue': {'label': 'Revenue'},
                    'profit': {'label': 'Profit'},
                }
            ),
            'shares': json.dumps(
                [
                    {'browser': 'Chrome', 'visitors': 275},
                    {'browser': 'Safari', 'visitors': 200},
                    {'browser': 'Firefox', 'visitors': 187},
                    {'browser': 'Edge', 'visitors': 173},
                    {'browser': 'Other', 'visitors': 90},
                ]
            ),
            'palette': json.dumps(
                {
                    name: {}
                    for name in (
                        'Chrome',
                        'Safari',
                        'Firefox',
                        'Edge',
                        'Other',
                    )
                }
            ),
        },
    )


urlpatterns = [
    path('', index, name='index'),
    path('submitted/', submitted, name='submitted'),
]

if __name__ == '__main__':
    django.setup()
    execute_from_command_line(sys.argv)
