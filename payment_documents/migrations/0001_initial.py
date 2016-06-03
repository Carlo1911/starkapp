# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-03 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=200)),
                ('amount', models.FloatField()),
                ('igv', models.FloatField()),
                ('realAmount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Document_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('descripcion', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='payment_document',
            name='payment_document_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment_documents.Payment_Document_Type'),
        ),
    ]
