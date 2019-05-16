# Generated by Django 2.1.8 on 2019-05-16 20:05

from django.db import migrations

def forward(apps, schema_editor):
    Appearance = apps.get_model('api.appearance')

    ps = Appearance.objects.filter(
        round__session__convention__status__lte=0,
        round__session__convention__year__gte=1994,
        representing='',
    )
    for p in ps:
        try:
            if p.group.kind == 32:
                representing = p.group.parent.parent.code
            else:
                representing = p.group.parent.code
        except AttributeError:
            representing = 'ERROR'
        p.representing = representing
        p.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_round_is_reviewed'),
    ]

    operations = [
        migrations.RunPython(forward),
    ]
