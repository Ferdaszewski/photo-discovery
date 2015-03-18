# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import visualize.models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0006_auto_20150318_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(height_field=b'height', width_field=b'width', upload_to=visualize.models.create_file_path),
            preserve_default=True,
        ),
    ]
