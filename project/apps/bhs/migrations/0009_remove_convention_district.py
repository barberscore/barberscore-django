# Generated by Django 2.2.3 on 2019-07-30 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bhs', '0008_auto_20190729_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convention',
            name='district',
        ),
    ]