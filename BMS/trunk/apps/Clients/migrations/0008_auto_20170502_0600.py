# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 06:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0007_auto_20170502_0528'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='concernperson',
            unique_together=set([('order', 'client')]),
        ),
    ]