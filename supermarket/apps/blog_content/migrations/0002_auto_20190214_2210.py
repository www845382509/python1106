# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-14 22:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_content', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='updata_time',
            new_name='update_time',
        ),
        migrations.RenameField(
            model_name='contentmodle',
            old_name='updata_time',
            new_name='update_time',
        ),
        migrations.RenameField(
            model_name='docket',
            old_name='updata_time',
            new_name='update_time',
        ),
    ]
