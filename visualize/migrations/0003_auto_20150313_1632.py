# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0002_auto_20150313_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='heigth',
            new_name='height',
        ),
    ]
