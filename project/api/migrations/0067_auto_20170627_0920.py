# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 16:20
from __future__ import unicode_literals

import api.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0066_auto_20170627_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=api.fields.PathAndRename()),
        ),
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=api.fields.PathAndRename()),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=api.fields.PathAndRename()),
        ),
    ]
