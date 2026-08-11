"""A Django project small enough to read, for looking at a component.

It renders `templates/index.html` against the components in this checkout
rather than a copy of them, so editing one and reloading is the whole loop.

    uv run python example/manage.py runserver
"""

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
    INSTALLED_APPS=['django.contrib.staticfiles', 'django_cotton'],
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


urlpatterns = [
    path('', lambda request: render(request, 'index.html'), name='index'),
    path('submitted/', submitted, name='submitted'),
]

if __name__ == '__main__':
    django.setup()
    execute_from_command_line(sys.argv)
