# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0015_remove_metadata_ac_color_sort_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='ac_hex_color_avg',
            field=models.CharField(max_length=7),
            preserve_default=True,
        ),
    ]
