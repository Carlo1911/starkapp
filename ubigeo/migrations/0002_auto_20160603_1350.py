# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubigeo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubigeo',
            name='status',
        ),
        migrations.AlterField(
            model_name='ubigeo',
            name='province',
            field=models.CharField(max_length=200),
        ),
    ]