from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
import json

from visualize.forms import NewAlbumForm
from visualize.models import Album, Photo


@login_required
def index(request):
    """Returns the main dashboard for logged in users."""
    return HttpResponse('Index!')


def visualize(request):
    return HttpResponse('A cool visualization!')


@login_required
def dashboard(request):

    # TEST
    user = request.user
    album = Album.objects.filter(user=user)[0]
    images = Photo.objects.filter(album=album)

    context_dict = {
        'user': user,
        'album': album,
        'images': images
    }

    return render(request, 'visualize/test.html', context_dict)


@login_required
def upload(request):
    return render(request, 'visualize/upload.html', {})


@login_required
def upload_image(request):
    if request.method == 'POST':
        user = request.user
        form = NewAlbumForm(request.POST, request.FILES)

        if form.is_valid():
            form_data = form.cleaned_data

            # Get album
            album = Album.objects.get(
                name=form_data['album_name'], user=user)

            # Add new photo to the album
            new_photo = Photo(original=form_data['image'])
            new_photo.album = album
            new_photo.original_name = str(form_data['image'].name)
            new_photo.save()

        return HttpResponse(json.dumps({'OK': 1}),
                            content_type="application/json")
    else:
        return HttpResponse("Error, POST only at this URL")


@login_required
def create_album(request):
    if request.method == 'POST' and request.POST.get('album_name'):
        new_album, created = Album.objects.get_or_create(
            name=request.POST.get('album_name'),
            user=request.user)
        if created:
            new_album.save()
            return HttpResponse(
                json.dumps({'success': True, 'error_message': None}),
                content_type='application/json')
    else:
        return HttpResponse("Error, POST only at this URL")

    # Album not created, return error
    return HttpResponse(
        json.dumps({'success': False,
                   'error_message': 'Already an album with that name!'}),
        content_type='application/json')
