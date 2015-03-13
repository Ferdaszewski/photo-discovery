from django.conf.urls import include, patterns, url
from visualize import views


urlpatterns = patterns(
    '',
    url(r'^$', views.visualize, name='visualize'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^upload/$', views.upload, name='upload'),
    )
