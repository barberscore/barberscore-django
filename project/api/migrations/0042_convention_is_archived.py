# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_remove_grantor_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='convention',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]