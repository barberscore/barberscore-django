# Generated by Django 2.1.8 on 2019-05-16 19:29

from django.db import migrations

def forward(apps, schema_editor):
    Award = apps.get_model('api.award')
    Round = apps.get_model('api.round')

    rs = Round.objects.filter(
        session__convention__status__lte=0,
        session__convention__year__gte=1994,
        outcomes__isnull=True,
    )
    for r in rs:
        ws = Award.objects.filter(
            kind=r.session.kind,
            season=r.session.convention.season,
            group=r.session.convention.group,
        )
        for w in ws:
            r.outcomes.create(
                award=w,
            )



class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190516_1008'),
    ]

    operations = [
        migrations.RunPython(forward),
    ]
