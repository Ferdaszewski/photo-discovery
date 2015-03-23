# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0011_auto_20150320_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visualizationmetadata',
            name='image_file',
        ),
        migrations.DeleteModel(
            name='VisualizationMetadata',
        ),
    ]
