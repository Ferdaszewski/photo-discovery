# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0007_auto_20150318_1047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image_file',
            new_name='original',
        ),
    ]
