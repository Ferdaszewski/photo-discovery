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
    return HttpResponse('User profile dashboard')


@login_required
def upload(request):
    return render(request, 'visualize/upload.html', {})


@login_required
def upload_image(request):
    if request.method == 'POST':
        user = request.user
        album_name = request.POST.get('album_name')
        image = request.FILES.get('image')

        # Create a new album
        new_album, _ = Album.objects.get_or_create(name=album_name, user=user)
        new_album.save()

        # Add new photo to the album
        new_photo = Photo(image_file=image)
        new_photo.album = new_album
        new_photo.original_name = str(image.name)
        new_photo.save()

        return HttpResponse(json.dumps({'OK': 1}), content_type="application/json")
    else:
        return HttpResponse("Error, POST only at this URL")
