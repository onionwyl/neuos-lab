# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='student_id',
        ),
        migrations.AddField(
            model_name='homework',
            name='self_check_result',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='homework',
            name='check_result',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
