# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 02:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160525_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_type_id',
        ),
    ]