# Generated by Django 2.1.2 on 2018-10-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0163_auto_20181017_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='complete',
            name='num_appearances',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complete',
            name='num_panelists',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complete',
            name='num_rounds',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
