from django.contrib.auth.models import User
from django.db import models
import uuid

from photodiscovery.settings import BASE_DIR


def create_file_path(instance, filename):
    """Helper function to create a file path for a photo."""
    album_id = instance.album.id
    new_filename = instance.photo_id + filename.split('.')[-1]

    return BASE_DIR + '/media/images/{0}/{1}'.format(album_id, new_filename)


def create_uuid():
    """Helper function to create a new random UUID for a primary key"""
    return uuid.uuid4().hex


class Album(models.Model):
    """User album to hold photos for the visualization."""
    user = models.ForeignKey(User)
    name = models.CharField(max_length=32, blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        # Users cannot have albums with the same name
        unique_together = ('user', 'name')


class Photo(models.Model):
    """Photos for an album."""
    photo_id = models.CharField(
        primary_key=True,
        max_length=32,
        default=create_uuid
        )
    album = models.ForeignKey(Album)
    image_file = models.ImageField(
        upload_to=create_file_path,
        blank=False,
        height_field='height',
        width_field='width',
        )
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.image_file.name


class VisualizationMetadata(models.Model):
    """Information from the processing of photos."""
    image_file = models.ForeignKey(Photo)

    # Average Color visualization data
    # Hex RBG of the average image color
    ac_hex_color_avg = models.CharField(max_length=6)
    ac_color_sort_order = models.IntegerField()

    def __unicode__(self):
        return self.image_file
