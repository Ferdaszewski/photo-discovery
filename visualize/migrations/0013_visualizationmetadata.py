# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0012_auto_20150322_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisualizationMetadata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ac_hex_color_avg', models.CharField(max_length=6)),
                ('ac_color_sort_order', models.IntegerField()),
                ('image_file', models.ForeignKey(to='visualize.Photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
