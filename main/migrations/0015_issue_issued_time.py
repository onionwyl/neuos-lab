# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20170817_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='issued_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]