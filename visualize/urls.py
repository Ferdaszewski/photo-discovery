from django.conf.urls import include, patterns, url
from visualize import views


urlpatterns = patterns(
    '',
    url(r'^$', views.visualize),
    url(r'^album/(?P<album_share_id>[0-9a-fA-F]{32})/$',
        views.visualize, name='public_album_visualize'),
    url(r'^album/(?P<album_name_slug>[\w\-]+)/$',
        views.visualize, name='album_visualize'),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/edit/albums/$', views.edit_albums, name='edit_albums'),
    url(r'^dashboard/edit/album/(?P<album_name_slug>[\w\-]+)/$',
        views.edit_album, name='edit_album'),

    url(r'^upload/$', views.upload, name='upload'),
    url(r'^upload/album/$', views.create_album, name='create_album'),
    url(r'^upload/image/$', views.upload_image, name='upload_image'),
    )
