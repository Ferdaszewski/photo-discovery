from django.conf.urls import include, patterns, url
from visualize import views


urlpatterns = patterns(
    '',
    url(r'^$', views.visualize, name='visualize'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^upload/album/$', views.create_album, name='create_album'),
    url(r'^upload/image/$', views.upload_image, name='upload_image'),
    )
