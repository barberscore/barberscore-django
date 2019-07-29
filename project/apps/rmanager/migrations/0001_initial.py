# Generated by Django 2.2.3 on 2019-07-29 00:16

import apps.rmanager.fields
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appearance',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-30, 'Disqualified'), (-20, 'Scratched'), (-10, 'Completed'), (0, 'New'), (7, 'Built'), (10, 'Started'), (20, 'Finished'), (25, 'Variance'), (30, 'Verified'), (40, 'Advanced')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('num', models.IntegerField(help_text='The order of appearance for this round.')),
                ('draw', models.IntegerField(blank=True, help_text='The draw for the next round.', null=True)),
                ('is_private', models.BooleanField(default=False, help_text='Copied from entry.')),
                ('is_single', models.BooleanField(default=False, help_text='Single-round group')),
                ('participants', models.CharField(blank=True, default='', help_text='Director(s) or Members (listed TLBB)', max_length=255)),
                ('representing', models.CharField(blank=True, default='', help_text='Representing entity', max_length=255)),
                ('onstage', models.DateTimeField(blank=True, help_text='\n            The actual appearance datetime.', null=True)),
                ('actual_start', models.DateTimeField(blank=True, help_text='\n            The actual appearance datetime.', null=True)),
                ('actual_finish', models.DateTimeField(blank=True, help_text='\n            The actual appearance datetime.', null=True)),
                ('pos', models.IntegerField(blank=True, help_text='Actual Participants-on-Stage', null=True)),
                ('stats', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('base', models.FloatField(blank=True, help_text='\n            The incoming base score used to determine most-improved winners.', null=True)),
                ('variance_report', models.FileField(blank=True, default='', upload_to=apps.rmanager.fields.UploadPath('variance_report'))),
                ('csa_report', models.FileField(blank=True, default='', upload_to=apps.rmanager.fields.UploadPath('csa_report'))),
                ('group_id', models.UUIDField(blank=True, null=True)),
            ],
            options={
                'ordering': ['num'],
            },
        ),
        migrations.CreateModel(
            name='Panelist',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Inactive'), (-5, 'Released'), (0, 'New'), (10, 'Active')], default=10, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('num', models.IntegerField(blank=True, null=True)),
                ('kind', models.IntegerField(choices=[(10, 'Official'), (20, 'Practice'), (30, 'Observer')])),
                ('category', models.IntegerField(blank=True, choices=[(5, 'DRCJ'), (10, 'CA'), (30, 'Music'), (40, 'Performance'), (50, 'Singing')], null=True)),
                ('psa_report', models.FileField(blank=True, default='', upload_to=apps.rmanager.fields.UploadPath('psa_report'))),
                ('representing', models.CharField(blank=True, default='', max_length=255)),
                ('person_id', models.UUIDField(blank=True, null=True)),
                ('owners', models.ManyToManyField(related_name='panelists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'New')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('num', models.IntegerField()),
                ('asterisks', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None)),
                ('dixons', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None)),
                ('penalties', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(choices=[(10, 'Primarily Patriotic/Religious Intent'), (30, 'Instrumental Accompaniment'), (40, 'Chorus Exceeding 4-Part Texture'), (50, 'Sound Equipment or Electronic Enhancement')]), blank=True, default=list, size=None)),
                ('stats', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('chart_id', models.UUIDField(blank=True, null=True)),
                ('appearance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='rmanager.Appearance')),
            ],
            options={
                'get_latest_by': ['num'],
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'New'), (10, 'Verified'), (25, 'Cleared'), (30, 'Flagged'), (35, 'Revised'), (40, 'Confirmed')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('points', models.IntegerField(blank=True, help_text='\n            The number of points (0-100)', null=True, validators=[django.core.validators.MaxValueValidator(100, message='Points must be between 0 - 100'), django.core.validators.MinValueValidator(0, message='Points must be between 0 - 100')])),
                ('panelist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='rmanager.Panelist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='rmanager.Song')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'New'), (10, 'Built'), (20, 'Started'), (25, 'Completed'), (27, 'Verified'), (30, 'Published')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('kind', models.IntegerField(choices=[(1, 'Finals'), (2, 'Semi-Finals'), (3, 'Quarter-Finals')])),
                ('num', models.IntegerField(default=0)),
                ('spots', models.IntegerField(default=0)),
                ('date', models.DateField(blank=True, null=True)),
                ('footnotes', models.TextField(blank=True, help_text='\n            Freeform text field; will print on OSS.')),
                ('oss_report', models.FileField(blank=True, default='', upload_to=apps.rmanager.fields.UploadPath('oss_report'))),
                ('sa_report', models.FileField(blank=True, default='', upload_to=apps.rmanager.fields.UploadPath('sa_report'))),
                ('legacy_oss', models.FileField(blank=True, default='', upload_to=apps.rmanager.fields.UploadPath('legacy_oss'))),
                ('is_reviewed', models.BooleanField(default=False, help_text='Reviewed for history app')),
                ('session_id', models.UUIDField(blank=True, null=True)),
                ('owners', models.ManyToManyField(related_name='rounds', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': ['num'],
            },
        ),
        migrations.AddField(
            model_name='panelist',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panelists', to='rmanager.Round'),
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(-10, 'Inactive'), (0, 'New'), (10, 'Active')], default=0)),
                ('num', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('award_name', models.CharField(blank=True, default='', max_length=1024)),
                ('award_id', models.UUIDField(blank=True, null=True)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcomes', to='rmanager.Round')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='appearance',
            name='outcomes',
            field=models.ManyToManyField(blank=True, related_name='appearances', to='rmanager.Outcome'),
        ),
        migrations.AddField(
            model_name='appearance',
            name='owners',
            field=models.ManyToManyField(related_name='appearances', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appearance',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appearances', to='rmanager.Round'),
        ),
    ]
