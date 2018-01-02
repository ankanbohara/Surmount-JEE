# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-08-21 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20170821_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=1000)),
                ('choice2', models.CharField(max_length=1000)),
                ('choice3', models.CharField(max_length=1000)),
                ('choice4', models.CharField(max_length=1000)),
                ('ques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='choices',
            name='ques',
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
    ]
