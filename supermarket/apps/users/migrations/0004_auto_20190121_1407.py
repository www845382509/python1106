# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-21 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190121_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='birth_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='hometown',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='school_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='sex',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], default=1),
        ),
    ]
