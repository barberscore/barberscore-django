# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 19:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20171213_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appearance',
            name='slot',
        ),
    ]