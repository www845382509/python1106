# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-21 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190121_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='tel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
