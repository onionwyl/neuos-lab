# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20170824_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework_id', models.IntegerField()),
                ('check_type', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
