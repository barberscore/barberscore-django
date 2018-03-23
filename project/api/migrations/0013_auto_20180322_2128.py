# Generated by Django 2.0.3 on 2018-03-23 04:22

from django.db import migrations


def forward(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    subs = [
        (10, 'RG', 'RG Regular'),
        (20, 'R5', 'R5 Regular 50 Year'),
        (30, 'SN', 'SN Senior'),
        (40, 'S5', 'S5 Senior 50 Year'),
        (50, 'SL', 'SL Senior Legacy'),
        (60, 'Y1', 'Y1 Youth Initial'),
        (70, 'Y2', 'Y2 Youth Subsequent'),
        (80, 'LF', 'LF Lifetime Regular'),
        (90, 'L5', 'L5 Lifetime 50 Year'),
        (100, 'LY', 'LY Lifetime Youth'),
        (110, 'LS', 'LS Lifetime Senior'),
        (120, 'AS', 'AS Associate'),
    ]

    Subscription = apps.get_model('api', 'Subscription')

    for s in subs:
        Subscription.objects.create(
            code=s[0],
            name=s[2],
            status=10,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_subscription'),
    ]

    operations = [
        migrations.RunPython(forward),
    ]
