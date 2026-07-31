"""Empty tag library standing in for third-party ones.

The allauth templates open with {% load account %}, which comes from
django-allauth. Installing it just to parse a template is not worth it, so
the load resolves here instead. If a component ever uses an actual tag from
one of those libraries, compilation fails with "Invalid block tag" and the
real library has to be installed.
"""

from django.template import Library

register = Library()
