# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-08-05 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siwedeeapp', '0015_catpersonas_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catpersonas',
            name='USUARIO',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]