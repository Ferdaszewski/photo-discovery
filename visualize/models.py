from django.contrib.auth.models import User
from django.db import models


class Album(models.Model):
    """User album to hold photos for the visualization."""
    user = models.ForeignKey(User)
    name = models.CharField(max_length=32, blank=False)


class Photo(models.Model):
    """Holds the photos for an album."""
    image_file = models.ImageField(
        upload_to='',
        blank=False,
        height_field='height',
        width_field='width')
    collection = models.ForeignKey(Album)


class VisualizationMetadata(models.Model):
    """Information from the processing of photos."""
    image_file = models.ForeignKey(Photo)

    # Average Color visualization data
    # Hex RBG average of the image (0xffffff == 16777215)
    ac_hex_color_avg = models.IntegerField(max_length=16777215)
    ac_color_sort_order = models.IntegerField()
