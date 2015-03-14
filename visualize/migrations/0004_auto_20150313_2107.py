# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import visualize.models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0003_auto_20150313_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='id',
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_id',
            field=models.CharField(default=visualize.models.create_uuid, max_length=32, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visualizationmetadata',
            name='ac_hex_color_avg',
            field=models.CharField(max_length=6),
            preserve_default=True,
        ),
    ]
