from django.contrib.auth.models import User
from django.db import models


def create_file_path(instance, filename):
    return '/user_images/{0}/{1}/{2}'.format(
        instance.album.user, instance.album.name, filename)


class Album(models.Model):
    """User album to hold photos for the visualization."""
    user = models.ForeignKey(User)
    name = models.CharField(max_length=32, blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('user', 'name')


class Photo(models.Model):
    """Photos for an album."""
    album = models.ForeignKey(Album)
    image_file = models.ImageField(
        upload_to=create_file_path,
        blank=False,
        height_field='height',
        width_field='width')

    def __unicode__(self):
        return self.image_file.name


class VisualizationMetadata(models.Model):
    """Information from the processing of photos."""
    image_file = models.ForeignKey(Photo)

    # Average Color visualization data
    # Hex RBG average of the image (0xffffff == 16777215)
    ac_hex_color_avg = models.IntegerField(max_length=16777215)
    ac_color_sort_order = models.IntegerField()

    def __unicode__(self):
        return self.image_file
