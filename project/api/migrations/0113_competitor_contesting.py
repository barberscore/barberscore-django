# Generated by Django 2.0.8 on 2018-09-14 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0112_round_legacy_oss'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='contesting',
            field=models.CharField(blank=True, default='', help_text='Award numbers contestanting', max_length=255),
        ),
    ]
