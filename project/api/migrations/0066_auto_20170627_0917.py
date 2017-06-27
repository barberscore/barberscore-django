# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 16:17
from __future__ import unicode_literals

import api.fields
import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0065_auto_20170626_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='image',
            field=models.FileField(blank=True, max_length=255, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to=api.fields.PathAndRename(prefix='chart')),
        ),
    ]
