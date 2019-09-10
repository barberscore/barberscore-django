# Generated by Django 2.2.5 on 2019-09-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_auto_20190909_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='chapters',
            field=models.CharField(blank=True, default='', help_text='The Chapter(s) that the comprise the group Members/Chorus.', max_length=255),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pos',
            field=models.IntegerField(blank=True, help_text='Estimated Participants-on-Stage (chorus only)', null=True),
        ),
    ]