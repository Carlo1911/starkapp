# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0001_initial'),
        ('activities', '0003_activity_activity_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='enviroment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='environment.Environment'),
            preserve_default=False,
        ),
    ]