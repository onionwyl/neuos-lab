# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20170826_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='pending',
            name='if_check',
            field=models.BooleanField(default=False),
        ),
    ]
