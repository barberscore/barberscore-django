# Generated by Django 2.1.8 on 2019-06-08 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grid',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grids', to='rmanager.Round'),
        ),
    ]
