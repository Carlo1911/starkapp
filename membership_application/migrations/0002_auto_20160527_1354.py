# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership_application',
            name='status',
            field=models.IntegerField(),
        ),
    ]
