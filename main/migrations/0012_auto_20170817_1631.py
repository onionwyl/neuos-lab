# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-17 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20170817_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='check_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='request_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
