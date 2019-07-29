# Generated by Django 2.2.3 on 2019-07-29 04:24

from django.db import migrations

def forward(apps, schema_editor):
    Appearance = apps.get_model('rmanager.appearance')
    Group = apps.get_model('bhs.group')
    ps = Appearance.objects.filter(
        group_id__isnull=False,
    )
    for p in ps:
        group = Group.objects.get(id=p.group_id)
        p.group_id = group.group_id
        p.group_status = group.group_status
        p.group_name = group.group_name
        p.group_nomen = group.group_nomen
        p.group_kind = group.group_kind
        p.group_gender = group.group_gender
        p.group_division = group.group_division
        p.group_bhs_id = group.group_bhs_id
        p.group_code = group.group_code
        p.group_description = group.group_description
        p.group_participants = group.group_participants
        p.group_tree_sort = group.group_tree_sort
        p.group_international = group.group_international
        p.group_district = group.group_district
        p.group_chapter = group.group_chapter
        p.group_is_senior = group.group_is_senior
        p.group_is_youth = group.group_is_youth
        p.group_is_divided = group.group_is_divided
        p.save()

class Migration(migrations.Migration):

    dependencies = [
        ('rmanager', '0002_auto_20190728_2123'),
    ]

    operations = [
    ]
