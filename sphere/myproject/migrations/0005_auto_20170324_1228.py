# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0004_auto_20170324_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='likemodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
