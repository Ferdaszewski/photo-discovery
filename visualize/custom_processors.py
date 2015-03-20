from visualize.models import Album


def albums(request):
    """Returns"""
    current_user = request.user
    if current_user.is_authenticated():
        user_album = Album.objects.filter(user=current_user)[:10]
        return {'albums': user_album}
    else:
        return {}
