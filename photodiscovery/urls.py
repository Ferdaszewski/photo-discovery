from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import redirect
from registration.backends.simple.views import RegistrationView


class MyRedirect(RegistrationView):
    """Redirects user to main page if success."""
    def get_success_url(self, request, user):
        return 'dashboard'


urlpatterns = patterns(
    '',
    url(r'^visualize/', include('visualize.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', MyRedirect.as_view(),
        name='registration_register'),
    url(r'^accounts/password/change/done/$', 'visualize.views.visualize'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', 'visualize.views.visualize'),
    )


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)', 'serve',
            {'document_root': settings.MEDIA_ROOT}))
