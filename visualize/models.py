from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, SmartResize
import itertools
import uuid


def create_file_path(instance, filename):
    """Helper function to create a file path for a photo."""
    album_id = instance.album.id
    new_filename = instance.photo_id + '.' + filename.split('.')[-1]

    return 'original_images/{1}'.format(album_id, new_filename)


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
        """Uniqueness is only guaranteed with user and name. But
        different names can result in the same slug. This function
        ensures automatically that a user's slug is unique to them.
        """
        self.slug = orig = slugify(self.name)
        for counter in itertools.count(1):
            if Album.objects.filter(slug=self.slug, user=self.user).exists():
                self.slug = '{}-{}'.format(orig, counter)
            else:
                break
        super(Album, self).save(*args, **kwargs)

    def photo_count(self):
        """Returns the number of images in the album (int)."""
        return Photo.objects.filter(album=self).count()

    def __unicode__(self):
        return self.name

    class Meta:
        """Users cannot have albums with the same name. Because of the
        save method, slugs will always be unique for the user on
        save, but it is still enforced at the database level.
        """
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

    def save(self, *args, **kwargs):
        """Generate web and thumbnail resolution versions of the image
        and save in the Imagekit Cache.
        """
        super(Photo, self).save(*args, **kwargs)
        self.web.generate()
        self.thumbnail.generate()

    def __unicode__(self):
        return self.original_name


class Metadata(models.Model):
    """Information from the processing of photos."""
    image_file = models.OneToOneField(Photo)

    # Primary Color visualization data
    # Web Hex RBG of the primary image color (i.e. '#fa0319')
    pc_hex = models.CharField(max_length=7)

    # YIQ conversion from the RGB values. Used for ordering by color
    pc_y = models.FloatField()
    pc_i = models.FloatField()
    pc_q = models.FloatField()

    # HSL converted from the RGB. Used for ordering by color
    pc_h = models.FloatField()
    pc_s = models.FloatField()
    pc_l = models.FloatField()

    def __unicode__(self):
        return self.image_file


@receiver(post_delete, sender=Photo)
def photo_post_delete_handler(sender, **kwargs):
    """Delete image files from storage after a photo is deleted from the
    database.
    """
    instance = kwargs.get('instance', None)

    if instance:
        # Delete the original file from storage.
        storage = instance.original.storage
        name = instance.original.name
        storage.delete(name)

        # Delete the Imagekit files from storage.
        storage = instance.web.storage
        storage.delete(instance.web.name)
        storage.delete(instance.thumbnail.name)
