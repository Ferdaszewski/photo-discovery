# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import visualize.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0005_photo_original_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=imagekit.models.fields.ProcessedImageField(height_field=b'height', width_field=b'width', upload_to=visualize.models.create_file_path),
            preserve_default=True,
        ),
    ]
