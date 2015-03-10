# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import visualize.models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='collection',
            new_name='album',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(height_field=b'height', width_field=b'width', upload_to=visualize.models.create_file_path),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together=set([('user', 'name')]),
        ),
    ]
