# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-08-04 23:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siwedeeapp', '0013_auto_20160804_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catpersonas',
            name='SEXO',
        ),
    ]