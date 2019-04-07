# Generated by Django 2.1.7 on 2019-04-04 19:39

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0116_auto_20190404_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panelist',
            name='status',
            field=django_fsm.FSMIntegerField(choices=[(-10, 'Inactive'), (-5, 'Completed'), (0, 'New'), (10, 'Active')], default=10, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.'),
        ),
    ]