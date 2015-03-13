from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView


# Redirects user to index page if successful at logging in
class MyRegistratoinView(RegistrationView):
    def get_success_url(self, request, user):
        return '/visualize/'

urlpatterns = patterns(
    '',
    url(r'^visualize/', include('visualize.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', MyRegistratoinView.as_view(),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', 'visualize.views.index'),
    )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)', 'serve',
            {'document_root': settings.MEDIA_ROOT}))
