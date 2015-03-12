from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from visualize.forms import NewAlbumForm
from visualize.models import Album, Photo


@login_required
def index(request):
    """Returns the main dashboard for logged in users."""
    return HttpResponse('Index!')


def visualize(request):
    return HttpResponse('A cool visulization!')


@login_required
def dashboard(request):
    return HttpResponse('User profile dashboard')


@login_required
def album_upload(request):
    user = request.user
    if request.method == 'POST':
        form = NewAlbumForm(request.POST)

        # Create new Album
        new_album = Album(
            user=user,
            name="test1")
        album = new_album.save()

        # Create new Photo for each uploaded image
        for uploaded_file in request.FILES.getlist('uploaded_files'):
            new_photo = Photo()
            new_photo.album = new_album
            new_photo.image_file = uploaded_file
            new_photo.save()


        if form.is_valid():
            new_album = form.save(commit=True, user=user)

        else:
            print form.errors

    # Not a HTTP POST, prep blank form for render
    else:
        form = NewAlbumForm()

    return render(request, 'visualize/upload.html', {'form': form})
