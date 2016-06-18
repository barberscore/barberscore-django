# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0068_slot_performance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='cursor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Performance'),
        ),
    ]
