# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-16 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170814_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.CharField(max_length=10)),
                ('issueid', models.CharField(max_length=10)),
                ('download', models.CharField(max_length=10)),
                ('repo', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('-studentid',),
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_percent', models.CharField(max_length=10)),
                ('pass_percent', models.CharField(max_length=10)),
            ],
        ),
    ]