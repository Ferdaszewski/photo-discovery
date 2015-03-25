# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0017_auto_20150324_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metadata',
            old_name='ac_hex_color_avg',
            new_name='pc_hex',
        ),
        migrations.AddField(
            model_name='metadata',
            name='pc_i',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metadata',
            name='pc_q',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metadata',
            name='pc_y',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
