from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

from .llms import llms_full_txt, llms_txt
from .views import home, page

# set_language stores the choice in a cookie, so it survives a visit to
# the bare domain later. It must sit outside the localized patterns.
urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

# English keeps the bare paths; the other languages get a prefix.
urlpatterns += i18n_patterns(
    path("", home, name="home"),
    path("llms.txt", llms_txt, name="llms"),
    path("llms-full.txt", llms_full_txt, name="llms-full"),
    path("<slug:slug>/", page, name="page"),
    prefix_default_language=False,
)
