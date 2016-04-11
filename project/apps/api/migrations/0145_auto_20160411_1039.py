# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0144_auto_20160410_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=255, unique=True)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, b'New')], default=0)),
                ('convention', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='api.Convention')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='api.Organization')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='host',
            unique_together=set([('organization', 'convention')]),
        ),
    ]
