# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-27 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siwedeeapp', '0005_auto_20160727_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='CATHISTREP',
            fields=[
                ('IDALUMNO', models.AutoField(primary_key=True, serialize=False)),
                ('FECHA_SUBIDA', models.DateField()),
                ('TIPO_REP', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CATMAESTROS',
            fields=[
                ('IDMAESTRO', models.AutoField(primary_key=True, serialize=False)),
                ('IDPERSONA', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CATPERSONAS',
            fields=[
                ('IDPERSONA', models.AutoField(primary_key=True, serialize=False)),
                ('IDTIPOPERSONA', models.IntegerField(null=True)),
                ('NOMBRE', models.CharField(max_length=50)),
                ('APELLIDO_PAT', models.CharField(max_length=50)),
                ('APELLIDO_MAT', models.CharField(max_length=50, null=True)),
                ('SEXO', models.CharField(max_length=1)),
                ('FECHA_NAC', models.DateField()),
                ('ACTIVO', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PERIODOESCOLAR',
            fields=[
                ('IDPERIODO', models.AutoField(primary_key=True, serialize=False)),
                ('NOMBRE', models.CharField(max_length=50)),
                ('FECHA_INI', models.DateField()),
                ('FECHA_FIN', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PROCESO',
            fields=[
                ('IDPROCESO', models.AutoField(primary_key=True, serialize=False)),
                ('ID_PERIODO', models.IntegerField()),
                ('NOMBRE', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='TIPOPERSONA',
            fields=[
                ('IDTIPOPERSONA', models.AutoField(primary_key=True, serialize=False)),
                ('NOMBRE', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='USUARIOS',
            fields=[
                ('IDPERSONA', models.AutoField(primary_key=True, serialize=False)),
                ('USUARIO', models.CharField(max_length=30)),
                ('PASSWORD', models.CharField(max_length=30)),
            ],
        ),
    ]
