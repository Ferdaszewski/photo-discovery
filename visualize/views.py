from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

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
def upload(request):
    if request.method == 'POST':
        user = request.user
        album_name = request.POST.get('album_name')
        image_list = request.FILES.getlist('image_list')

        # Create a new album
        new_album, _ = Album.objects.get_or_create(name=album_name, user=user)
        new_album.save()

        # Add new photos to the album
        for image in image_list:
            new_photo = Photo(image_file=image)
            new_photo.album = new_album
            new_photo.save()

        return redirect('dashboard')
    return render(request, 'visualize/upload.html', {})
