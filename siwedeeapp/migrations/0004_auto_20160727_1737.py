# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-27 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siwedeeapp', '0003_auto_20160727_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asigna_empresa',
            name='id',
        ),
        migrations.AlterField(
            model_name='asigna_empresa',
            name='IDASIGNA',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
