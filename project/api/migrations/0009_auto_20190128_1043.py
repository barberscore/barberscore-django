# Generated by Django 2.1.5 on 2019-01-28 18:43

from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190120_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(-25, 'Manual'), (-20, 'Incomplete'), (-15, 'Imported'), (-10, 'Inactive'), (0, 'New'), (10, 'Active')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.'),
        ),
        migrations.AlterField(
            model_name='round',
            name='oss',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to=''),
        ),
    ]
