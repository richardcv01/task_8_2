# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-11 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_auto_20170511_1733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cryptocurrency_table',
            options={'ordering': ['-insert_date'], 'verbose_name': 'coint'},
        ),
    ]
