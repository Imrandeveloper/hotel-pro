# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-04 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20180201_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chief',
            name='phones',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='phones',
        ),
    ]
