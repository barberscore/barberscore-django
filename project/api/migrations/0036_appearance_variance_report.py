# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-20 18:08
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20180119_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='appearance',
            name='variance_report',
            field=cloudinary.models.CloudinaryField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]
