# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='national_id',
            field=models.CharField(max_length=20, null=True, verbose_name='national id'),
        ),
    ]
