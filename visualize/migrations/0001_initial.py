# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import visualize.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_file', models.ImageField(height_field=b'height', width_field=b'width', upload_to=visualize.models.create_file_path)),
                ('width', models.IntegerField(blank=True)),
                ('heigth', models.IntegerField(blank=True)),
                ('album', models.ForeignKey(to='visualize.Album')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisualizationMetadata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ac_hex_color_avg', models.IntegerField(max_length=16777215)),
                ('ac_color_sort_order', models.IntegerField()),
                ('image_file', models.ForeignKey(to='visualize.Photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together=set([('user', 'name')]),
        ),
    ]
