# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-08-21 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20170821_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice',
        ),
    ]
