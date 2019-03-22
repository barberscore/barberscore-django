# Generated by Django 2.1.7 on 2019-03-22 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0065_auto_20190322_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appearance',
            name='mus_points',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='mus_rank',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='mus_score',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='per_points',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='per_rank',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='per_score',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='sng_points',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='sng_rank',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='sng_score',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='tot_points',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='tot_rank',
        ),
        migrations.RemoveField(
            model_name='appearance',
            name='tot_score',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='is_ranked',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='mus_points',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='mus_rank',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='mus_score',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='per_points',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='per_rank',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='per_score',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='sng_points',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='sng_rank',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='sng_score',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='tot_points',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='tot_rank',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='tot_score',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='mus_points',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='mus_rank',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='mus_score',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='per_points',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='per_rank',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='per_score',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='sng_points',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='sng_rank',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='sng_score',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='tot_points',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='tot_rank',
        ),
        migrations.RemoveField(
            model_name='contender',
            name='tot_score',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='mus_points',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='mus_rank',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='mus_score',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='per_points',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='per_rank',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='per_score',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='sng_points',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='sng_rank',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='sng_score',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='tot_points',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='tot_rank',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='tot_score',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='mus_points',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='mus_rank',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='mus_score',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='per_points',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='per_rank',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='per_score',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='sng_points',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='sng_rank',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='sng_score',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='tot_points',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='tot_rank',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='tot_score',
        ),
        migrations.RemoveField(
            model_name='song',
            name='mus_points',
        ),
        migrations.RemoveField(
            model_name='song',
            name='mus_rank',
        ),
        migrations.RemoveField(
            model_name='song',
            name='mus_score',
        ),
        migrations.RemoveField(
            model_name='song',
            name='per_points',
        ),
        migrations.RemoveField(
            model_name='song',
            name='per_rank',
        ),
        migrations.RemoveField(
            model_name='song',
            name='per_score',
        ),
        migrations.RemoveField(
            model_name='song',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='song',
            name='sng_points',
        ),
        migrations.RemoveField(
            model_name='song',
            name='sng_rank',
        ),
        migrations.RemoveField(
            model_name='song',
            name='sng_score',
        ),
        migrations.RemoveField(
            model_name='song',
            name='tot_points',
        ),
        migrations.RemoveField(
            model_name='song',
            name='tot_rank',
        ),
        migrations.RemoveField(
            model_name='song',
            name='tot_score',
        ),
    ]
