# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=posts.models.upload_location, width_field='width_field'),
        ),
    ]
