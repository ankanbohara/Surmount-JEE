# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-08-21 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20170817_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='choice1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choice2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choice3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choice4',
        ),
        migrations.AddField(
            model_name='choices',
            name='ques',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Question'),
        ),
    ]
