from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, SmartResize
import uuid

from photodiscovery.settings import BASE_DIR


def create_file_path(instance, filename):
    """Helper function to create a file path for a photo."""
    album_id = instance.album.id
    new_filename = instance.photo_id + '.' + filename.split('.')[-1]

    return BASE_DIR + '/media/images/{0}/{1}'.format(album_id, new_filename)


def create_uuid():
    """Helper function to create a new random UUID"""
    return uuid.uuid4().hex


class Album(models.Model):
    """User album holds photos."""
    share_id = models.CharField(max_length=32, default=create_uuid)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=32, blank=False)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        # Users cannot have albums with the same name
        unique_together = (('user', 'slug'), ('user', 'name'))


class Photo(models.Model):
    """Photos for an album."""
    photo_id = models.CharField(
        primary_key=True,
        max_length=32,
        default=create_uuid
        )
    album = models.ForeignKey(Album)
    original = models.ImageField(
        upload_to=create_file_path,
        blank=False,
        height_field='height',
        width_field='width',
        )

    # Imagekit specs
    web = ImageSpecField(
        source='original',
        processors=[ResizeToFit(
            width=1200,
            height=790,
            upscale=False,
            )],
        format='JPEG',
        options={'quality': 90}
        )
    thumbnail = ImageSpecField(
        source='original',
        processors=[SmartResize(
            width=100,
            height=100,
            upscale=False,
            )],
        format='JPEG',
        options={'quality': 70},
        )

    original_name = models.CharField(max_length=255, blank=False)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.original_name


class VisualizationMetadata(models.Model):
    """Information from the processing of photos."""
    image_file = models.ForeignKey(Photo)

    # Average Color visualization data
    # Hex RBG of the average image color
    ac_hex_color_avg = models.CharField(max_length=6)
    ac_color_sort_order = models.IntegerField()

    def __unicode__(self):
        return self.image_file
