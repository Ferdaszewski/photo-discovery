# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0004_auto_20150313_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='original_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
