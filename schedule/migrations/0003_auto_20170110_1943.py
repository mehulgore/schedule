# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-10 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20170110_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='time_sheet',
            field=models.CharField(max_length=200),
        ),
    ]
