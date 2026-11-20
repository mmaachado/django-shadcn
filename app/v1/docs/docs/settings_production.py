from .settings import *

DEBUG = False

# The base settings fall back to a key published in this repository, so a
# deploy that forgot to set one would sign with a key anyone can read.
SECRET_KEY = env("DJANGO_SECRET_KEY", default="")

if not SECRET_KEY or SECRET_KEY.startswith("django-insecure-"):
    raise ImproperlyConfigured("DJANGO_SECRET_KEY must be set in production")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Django security checklist settings
# More details here: https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HTTP Strict Transport Security settings
# https://docs.djangoproject.com/en/dev/ref/middleware/#http-strict-transport-security
# Preloading would need a year of max-age, and a vercel.app host cannot be
# preloaded anyway.
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

USE_HTTPS_IN_ABSOLUTE_URLS = True

# Every deploy also answers on a generated *.vercel.app host, and a preview
# gets a fresh one on each push, so the host is matched by suffix.
ALLOWED_HOSTS = [
    "django-shadcn.com",
    ".vercel.app",
]
# Only cross-origin posts need trusting: a deploy posting to itself passes
# the same-origin check on its own, whatever its host. The wildcard trusted
# every site on vercel.app.
CSRF_TRUSTED_ORIGINS = [
    "https://django-shadcn.com",
]
