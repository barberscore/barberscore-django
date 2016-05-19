# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20160519_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='award',
            old_name='num_rounds',
            new_name='championship_rounds',
        ),
        migrations.AlterField(
            model_name='award',
            name='is_improved',
            field=models.BooleanField(default=False, help_text=b"Designates 'Most-Improved'.  Implies manual."),
        ),
        migrations.AlterField(
            model_name='award',
            name='is_manual',
            field=models.BooleanField(default=False, help_text=b'Award must be determined manually.'),
        ),
        migrations.AlterField(
            model_name='award',
            name='is_primary',
            field=models.BooleanField(default=False, help_text=b'No secondary award critera.'),
        ),
    ]
