# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 04:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20170217_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performerscore',
            name='performer_ptr',
        ),
        migrations.DeleteModel(
            name='PerformerScore',
        ),
    ]
