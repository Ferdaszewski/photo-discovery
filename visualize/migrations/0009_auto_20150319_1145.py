# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import visualize.models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0008_auto_20150318_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='share_id',
            field=models.CharField(default=visualize.models.create_uuid, max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together=set([('user', 'slug'), ('user', 'name')]),
        ),
    ]
