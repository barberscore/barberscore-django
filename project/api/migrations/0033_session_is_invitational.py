# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_person_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='is_invitational',
            field=models.BooleanField(default=False),
        ),
    ]
