# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.BigIntegerField()),
                ('businessName', models.CharField(max_length=120)),
                ('status', models.IntegerField(choices=[(0, 'Inactivo'), (1, 'Activo')], default=1)),
                ('region', models.CharField(max_length=120)),
                ('province', models.CharField(max_length=120)),
                ('distric', models.CharField(max_length=120)),
                ('registrationDate', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('postal', models.IntegerField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('contactName', models.CharField(max_length=120)),
                ('contactPhone', models.BigIntegerField()),
            ],
        ),
    ]
