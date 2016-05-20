# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 15:11
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20160520_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='original',
            field=models.IntegerField(blank=True, help_text=b'\n            The original score (before revision).', null=True, validators=[django.core.validators.MaxValueValidator(100, message=b'Points must be between 0 - 100'), django.core.validators.MinValueValidator(0, message=b'Points must be between 0 - 100')]),
        ),
    ]
