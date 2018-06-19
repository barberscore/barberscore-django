# Generated by Django 2.0.6 on 2018-06-18 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20180617_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='footnotes',
            field=models.TextField(blank=True, help_text='\n            Freeform text field; will print on OSS.'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contests', to='api.Group'),
        ),
    ]