from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
import json

from visualize.forms import NewAlbumForm
from visualize.image_processors import process_image
from visualize.models import Album, Photo


def round_float(photo):
    """Helper function that returns the photo.metadata attribute rounded
    down. For use when sorting photos by color."""

    # Column names to sort by and the precision
    sort_by = [('pc_h', 1), ('pc_i', 4), ('pc_q', 0)]

    sort_values = [round(getattr(photo.metadata, attr[0]), attr[1])
                   for attr in sort_by]
    return sort_values


def sort_photos(photo_list):
    """Sorts a list of Photo objects in place by color."""
    sorted_photo_list = sorted(photo_list, key=round_float)
    return sorted_photo_list


def visualize(request, album_name_slug=None, album_share_id=None):
    album = None

    # The only way to view an album without logging in is with the UUID
    # in album.share_id.
    if album_share_id:
        try:
            album = Album.objects.get(share_id=album_share_id)
        except Album.DoesNotExist:
            error = "Album does not exist with ID of: ", album_share_id

    elif request.user.is_authenticated():
        user = request.user
        if album_name_slug:
            try:
                album = Album.objects.get(slug=album_name_slug, user=user)
            except Album.DoesNotExist:
                error = "Album does not exist with slug of: ", album_name_slug

        # If no slug is provided, try to get the user's first album.
        else:
            try:
                album = Album.objects.filter(user=user)[0]

                # Redirect so user sees the correct slug url
                return redirect('album_visualize',
                                album_name_slug=album.slug)

            except IndexError:
                error = "You do not have any albums yet."

    # User not logged in and did not use a valid share_id
    else:
        return redirect('/accounts/login/')

    if album:

        # Order by YIQ to get a visually smooth sort order.
        # The alternatives (RGB or HSV) do not look sorted as they are
        # not based on human perception of color.
        images = Photo.objects.filter(album=album)

        # Sorts the list of Photo Objects by color
        images = sort_photos(images)

        context_dict = {
            'album': album,
            'images': images
        }

    # An album was not found, return the error
    else:
        context_dict = {'error': error}

    return render(request, 'visualize/visualize.html', context_dict)


@login_required
def dashboard(request):
    return render(request, 'visualize/dashboard.html')


@login_required
def edit_albums(request):
    """On GET display all the user's albums. POST is an AJAX call to
    delete an album.
    """
    if request.method == 'POST':
        user = request.user
        album_id = request.POST['id']
        album = Album.objects.get(user=user, id=album_id)
        album.delete()
        return HttpResponse(json.dumps({'OK': 1, 'share_id': album.share_id}),
                            content_type="application/json")
    else:
        return render(request, 'visualize/update_albums.html')


@login_required
def edit_album(request, album_name_slug):
    """On GET display all the user's phots in the album. POST is and
    AJAX call to delete a photo from the album.
    """
    user = request.user
    try:
        album = Album.objects.get(slug=album_name_slug, user=user)
    except Album.DoesNotExist:
        raise Http404

    # POST is send to delete a photo from an album
    if request.method == 'POST':
        photo_id = request.POST['id']
        photo = Photo.objects.get(album=album, photo_id=photo_id)
        photo.delete()
        return HttpResponse(json.dumps({'OK': 1}),
                            content_type="application/json")

    # Not POST, so get album photos and display
    else:
        photos = Photo.objects.filter(album=album)
        context_dict = {
            'album': album,
            'photos': photos,
        }
        return render(request, 'visualize/update_album.html', context_dict)


@login_required
def upload(request):
    return render(request, 'visualize/upload.html')


@login_required
def upload_image(request):
    """POST AJAX endpoint for adding a photo to a user's album."""
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

            # Process image
            process_image(new_photo)

        return HttpResponse(json.dumps({'OK': 1}),
                            content_type="application/json")
    else:
        return HttpResponse("Error, POST only at this URL")


@login_required
def create_album(request):
    """POST AJAX endpoint for creating an album."""
    if request.method == 'POST' and request.POST.get('album_name'):
        new_album, created = Album.objects.get_or_create(
            name=request.POST.get('album_name'),
            user=request.user)
        if created:
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
