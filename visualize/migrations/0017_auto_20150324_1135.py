# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0016_auto_20150323_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='image_file',
            field=models.OneToOneField(to='visualize.Photo'),
            preserve_default=True,
        ),
    ]
