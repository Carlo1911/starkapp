# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fine',
            old_name='fine_type_id',
            new_name='fine_type',
        ),
    ]