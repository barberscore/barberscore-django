# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 05:07
from __future__ import unicode_literals

import app.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20170217_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongPrivate',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('song', app.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Song')),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('mus_points', models.IntegerField(blank=True, null=True)),
                ('prs_points', models.IntegerField(blank=True, null=True)),
                ('sng_points', models.IntegerField(blank=True, null=True)),
                ('total_points', models.IntegerField(blank=True, null=True)),
                ('mus_score', models.FloatField(blank=True, null=True)),
                ('prs_score', models.FloatField(blank=True, null=True)),
                ('sng_score', models.FloatField(blank=True, null=True)),
                ('total_score', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
