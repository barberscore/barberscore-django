# Generated by Django 2.0.3 on 2018-03-19 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180319_1342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['tree_sort'], 'verbose_name_plural': 'groups'},
        ),
    ]