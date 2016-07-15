# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0099_auto_20160715_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='judge',
            old_name='bhs_panel_id',
            new_name='bhs_id',
        ),
        migrations.RemoveField(
            model_name='group',
            name='bhs_chapter_code',
        ),
        migrations.RemoveField(
            model_name='group',
            name='bhs_chapter_name',
        ),
        migrations.RemoveField(
            model_name='group',
            name='bhs_contact',
        ),
        migrations.RemoveField(
            model_name='group',
            name='bhs_district',
        ),
        migrations.RemoveField(
            model_name='group',
            name='bhs_expiration',
        ),
        migrations.RemoveField(
            model_name='group',
            name='bhs_location',
        ),
        migrations.RemoveField(
            model_name='group',
            name='bhs_name',
        ),
        migrations.RemoveField(
            model_name='group',
            name='bhs_phone',
        ),
        migrations.RemoveField(
            model_name='group',
            name='bhs_website',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_address',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_chapter_code',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_chapter_name',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_city',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_contact',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_district',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_group_name',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_name',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_phone',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_state',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_venue',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_website',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='bhs_zip',
        ),
        migrations.RemoveField(
            model_name='person',
            name='bhs_city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='bhs_email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='bhs_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='bhs_phone',
        ),
        migrations.RemoveField(
            model_name='person',
            name='bhs_state',
        ),
        migrations.RemoveField(
            model_name='role',
            name='bhs_file',
        ),
        migrations.RemoveField(
            model_name='session',
            name='entry_form',
        ),
        migrations.RemoveField(
            model_name='session',
            name='song_list',
        ),
    ]
