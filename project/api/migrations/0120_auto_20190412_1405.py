# Generated by Django 2.1.8 on 2019-04-12 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0119_auto_20190410_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='appearance',
            name='base',
            field=models.FloatField(blank=True, help_text='\n            The incoming base score used to determine most-improved winners.', null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='base',
            field=models.FloatField(blank=True, help_text='\n            The incoming base score used to determine most-improved winners.', null=True),
        ),
    ]