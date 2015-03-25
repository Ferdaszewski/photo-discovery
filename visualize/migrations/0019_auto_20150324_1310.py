# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0018_auto_20150324_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='pc_h',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metadata',
            name='pc_l',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metadata',
            name='pc_s',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
