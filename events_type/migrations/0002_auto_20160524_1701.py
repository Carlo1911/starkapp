# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 17:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events_type', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventType',
            new_name='EventsType',
        ),
    ]