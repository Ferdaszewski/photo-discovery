from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import json

from visualize.forms import NewAlbumForm
from visualize.image_processors import process_image
from visualize.models import Album, Photo


def sort_by(photo):
    """Helper function that returns the photo.metadata attributes as a
    tuple with their values rounded down. For use when sorting photos
    by color.
    """
    # Column names to sort by and the precision to round the values to.
    sort_list = [('pc_h', 1), ('pc_i', 4), ('pc_q', 0)]

    sort_values = [round(getattr(photo.metadata, i[0]), i[1])
                   for i in sort_list]
    return sort_values


def sort_photos(photo_list):
    """Sorts a list of Photo objects in place by color."""
    sorted_photo_list = sorted(photo_list, key=sort_by)
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
            'images': images,
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
        return JsonResponse({'OK': 1, 'share_id': album.share_id})
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
        return JsonResponse({'OK': 1})

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

        return JsonResponse({'OK': 1})

    # Not a POST, not other HTTP verbs for this view.
    else:
        raise Http404


@login_required
def create_album(request):
    """POST AJAX endpoint for creating an album and checking album name
    uniqueness.
    """
    if request.method == 'POST':

        # Get data from request payload
        user = request.user

        data = json.loads(request.body)
        album_name = data['album_name']
        album_create = data['album_create']

        # Default responses
        unique = False
        created = False
        message_text = None

        # Try to create the album
        if album_create:
            new_album, created = Album.objects.get_or_create(
                name=album_name,
                user=user)

            # New album created
            if created:
                unique = True
                created = True
                message_text = str(new_album)

            # Error, album already exists with name of album_name
            else:
                message_text = "{} already exists!".format(new_album)

        # Check that the album_name is unique but don't create album
        else:
            unique = not Album.objects.filter(
                name=album_name, user=user).exists()
            if not unique:
                message_text = "{} already exists!".format(album_name)

        # Return JSON response
        return JsonResponse({
            'unique': unique,
            'created': created,
            'message_text': message_text
            })

    # Not a POST, not other HTTP verbs for this view.
    else:
        raise Http404
