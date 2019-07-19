# Generated by Django 2.2.3 on 2019-07-19 16:05

import django.contrib.postgres.fields.ranges
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smanager', '0012_auto_20190719_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='award_age',
            field=models.IntegerField(blank=True, choices=[(10, 'Seniors'), (20, 'Novice'), (30, 'Youth')], null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_description',
            field=models.TextField(blank=True, help_text='\n            The Public description of the award.', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_district',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_division',
            field=models.IntegerField(blank=True, choices=[(10, 'EVG Division I'), (20, 'EVG Division II'), (30, 'EVG Division III'), (40, 'EVG Division IV'), (50, 'EVG Division V'), (60, 'FWD Arizona'), (70, 'FWD Northeast'), (80, 'FWD Northwest'), (90, 'FWD Southeast'), (100, 'FWD Southwest'), (110, 'LOL 10000 Lakes'), (120, 'LOL Division One'), (130, 'LOL Northern Plains'), (140, 'LOL Packerland'), (150, 'LOL Southwest'), (170, 'MAD Central'), (180, 'MAD Northern'), (190, 'MAD Southern'), (210, 'NED Granite and Pine'), (220, 'NED Mountain'), (230, 'NED Patriot'), (240, 'NED Sunrise'), (250, 'NED Yankee'), (260, 'SWD Northeast'), (270, 'SWD Northwest'), (280, 'SWD Southeast'), (290, 'SWD Southwest')], null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_gender',
            field=models.IntegerField(blank=True, choices=[(10, 'Male'), (20, 'Female'), (30, 'Mixed')], help_text='\n            The gender to which the award is restricted.  If unselected, this award is open to all combinations.\n        ', null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_is_novice',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_kind',
            field=models.IntegerField(blank=True, choices=[(32, 'Chorus'), (41, 'Quartet')], null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_level',
            field=models.IntegerField(blank=True, choices=[(10, 'Championship'), (30, 'Qualifier'), (45, 'Representative'), (50, 'Deferred'), (60, 'Manual'), (70, 'Improved - Raw'), (80, 'Improved - Standard')], null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_name',
            field=models.CharField(blank=True, help_text='Award Name.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_scope',
            field=models.IntegerField(blank=True, choices=[(100, 'Plateau 1'), (110, 'Plateau 2'), (120, 'Plateau 3'), (130, 'Plateau 4'), (140, 'Plateau A'), (150, 'Plateau AA'), (160, 'Plateau AAA'), (170, 'Plateau AAAA'), (175, 'Plateau AAAAA')], null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_scope_range',
            field=django.contrib.postgres.fields.ranges.DecimalRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_season',
            field=models.IntegerField(blank=True, choices=[(1, 'Summer'), (2, 'Midwinter'), (3, 'Fall'), (4, 'Spring')], null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_size',
            field=models.IntegerField(blank=True, choices=[(100, 'Plateau 1'), (110, 'Plateau 2'), (120, 'Plateau 3'), (130, 'Plateau 4'), (140, 'Plateau A'), (150, 'Plateau AA'), (160, 'Plateau AAA'), (170, 'Plateau AAAA'), (180, 'Plateau B'), (190, 'Plateau I'), (200, 'Plateau II'), (210, 'Plateau III'), (220, 'Plateau IV'), (230, 'Small')], null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_size_range',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='award_tree_sort',
            field=models.IntegerField(blank=True, editable=False, null=True, unique=True),
        ),
    ]