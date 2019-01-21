# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-21 13:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190119_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(11, '用户名为11位')]),
        ),
    ]
