# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_auto_20171106_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='grantor',
            name='convention',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grantors', to='api.Convention'),
        ),
    ]