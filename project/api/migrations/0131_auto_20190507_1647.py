# Generated by Django 2.1.8 on 2019-05-07 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0130_auto_20190507_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convention',
            name='venue',
            field=models.ForeignKey(blank=True, help_text='\n            The venue for the convention.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conventions', to='stage.Venue'),
        ),
    ]