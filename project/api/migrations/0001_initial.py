# Generated by Django 2.1.8 on 2019-05-14 16:51

import api.fields
import cloudinary_storage.storage
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.fields.ranges
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm
import model_utils.fields
import timezone_field.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bhs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', api.fields.LowerEmailField(blank=True, help_text='\n            The contact email of the resource.', max_length=254, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_convention_manager', models.BooleanField(default=False)),
                ('is_session_manager', models.BooleanField(default=False)),
                ('is_round_manager', models.BooleanField(default=False)),
                ('is_scoring_manager', models.BooleanField(default=False)),
                ('is_group_manager', models.BooleanField(default=False)),
                ('is_person_manager', models.BooleanField(default=False)),
                ('is_award_manager', models.BooleanField(default=False)),
                ('is_officer_manager', models.BooleanField(default=False)),
                ('is_chart_manager', models.BooleanField(default=False)),
                ('is_assignment_manager', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
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
                ('actual_start', models.DateTimeField(blank=True, help_text='\n            The actual appearance datetime.', null=True)),
                ('actual_finish', models.DateTimeField(blank=True, help_text='\n            The actual appearance datetime.', null=True)),
                ('pos', models.IntegerField(blank=True, help_text='Actual Participants-on-Stage', null=True)),
                ('legacy_num', models.IntegerField(blank=True, null=True)),
                ('stats', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('base', models.FloatField(blank=True, help_text='\n            The incoming base score used to determine most-improved winners.', null=True)),
                ('variance_report', models.FileField(blank=True, default='', upload_to=api.fields.FileUploadPath())),
                ('csa', models.FileField(blank=True, default='', upload_to=api.fields.FileUploadPath())),
            ],
            options={
                'ordering': ['-round__num', 'num'],
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Inactive'), (0, 'New'), (10, 'Active')], default=10, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('kind', models.IntegerField(choices=[(10, 'Official'), (20, 'Practice'), (30, 'Observer')])),
                ('category', models.IntegerField(blank=True, choices=[(5, 'DRCJ'), (10, 'CA'), (30, 'Music'), (40, 'Performance'), (50, 'Singing')], null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Award Name.', max_length=255)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Inactive'), (0, 'New'), (10, 'Active')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('kind', models.IntegerField(choices=[(32, 'Chorus'), (41, 'Quartet')])),
                ('gender', models.IntegerField(choices=[(10, 'Male'), (20, 'Female'), (30, 'Mixed')], default=10, help_text='\n            The gender of session.\n        ')),
                ('level', models.IntegerField(choices=[(10, 'Championship'), (30, 'Qualifier'), (45, 'Representative'), (50, 'Deferred'), (60, 'Manual'), (70, 'Improved - Raw'), (80, 'Improved - Standard')])),
                ('season', models.IntegerField(choices=[(1, 'Summer'), (2, 'Midwinter'), (3, 'Fall'), (4, 'Spring')])),
                ('is_single', models.BooleanField(default=False, help_text='Single-round award')),
                ('threshold', models.FloatField(blank=True, help_text='\n            The score threshold for automatic qualification (if any.)\n        ', null=True)),
                ('minimum', models.FloatField(blank=True, help_text='\n            The minimum score required for qualification (if any.)\n        ', null=True)),
                ('advance', models.FloatField(blank=True, help_text='\n            The score threshold to advance to next round (if any) in\n            multi-round qualification.\n        ', null=True)),
                ('spots', models.IntegerField(blank=True, help_text='Number of top spots which qualify', null=True)),
                ('description', models.TextField(blank=True, help_text='\n            The Public description of the award.', max_length=1000)),
                ('notes', models.TextField(blank=True, help_text='\n            Private Notes (for internal use only).')),
                ('division', models.IntegerField(blank=True, choices=[(10, 'EVG Division I'), (20, 'EVG Division II'), (30, 'EVG Division III'), (40, 'EVG Division IV'), (50, 'EVG Division V'), (60, 'FWD Arizona'), (70, 'FWD Northeast'), (80, 'FWD Northwest'), (90, 'FWD Southeast'), (100, 'FWD Southwest'), (110, 'LOL 10000 Lakes'), (120, 'LOL Division One'), (130, 'LOL Northern Plains'), (140, 'LOL Packerland'), (150, 'LOL Southwest'), (170, 'MAD Central'), (180, 'MAD Northern'), (190, 'MAD Southern'), (210, 'NED Granite and Pine'), (220, 'NED Mountain'), (230, 'NED Patriot'), (240, 'NED Sunrise'), (250, 'NED Yankee'), (260, 'SWD Northeast'), (270, 'SWD Northwest'), (280, 'SWD Southeast'), (290, 'SWD Southwest')], null=True)),
                ('age', models.IntegerField(blank=True, choices=[(10, 'Seniors'), (20, 'Novice'), (30, 'Youth')], null=True)),
                ('size', models.IntegerField(blank=True, choices=[(100, 'Plateau 1'), (110, 'Plateau 2'), (120, 'Plateau 3'), (130, 'Plateau 4'), (140, 'Plateau A'), (150, 'Plateau AA'), (160, 'Plateau AAA'), (170, 'Plateau AAAA'), (180, 'Plateau B'), (190, 'Plateau I'), (200, 'Plateau II'), (210, 'Plateau III'), (220, 'Plateau IV'), (230, 'Small')], null=True)),
                ('size_range', django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, null=True)),
                ('scope', models.IntegerField(blank=True, choices=[(100, 'Plateau 1'), (110, 'Plateau 2'), (120, 'Plateau 3'), (130, 'Plateau 4'), (140, 'Plateau A'), (150, 'Plateau AA'), (160, 'Plateau AAA'), (170, 'Plateau AAAA'), (175, 'Plateau AAAAA')], null=True)),
                ('scope_range', django.contrib.postgres.fields.ranges.FloatRangeField(blank=True, null=True)),
                ('tree_sort', models.IntegerField(blank=True, editable=False, null=True, unique=True)),
            ],
            options={
                'ordering': ['tree_sort'],
            },
        ),
        migrations.CreateModel(
            name='Contender',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Excluded'), (0, 'New'), (10, 'Included')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
            ],
            options={
                'ordering': ('outcome__num',),
            },
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Excluded'), (0, 'New'), (10, 'Included')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('is_primary', models.BooleanField(default=False)),
                ('result', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(-10, 'Excluded'), (0, 'New'), (10, 'Included')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
            ],
            options={
                'ordering': ('contest__award__tree_sort',),
            },
        ),
        migrations.CreateModel(
            name='Convention',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('legacy_name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('legacy_selection', models.CharField(blank=True, max_length=255, null=True)),
                ('legacy_complete', models.CharField(blank=True, max_length=255, null=True)),
                ('legacy_venue', models.CharField(blank=True, max_length=255, null=True)),
                ('status', django_fsm.FSMIntegerField(choices=[(-25, 'Manual'), (-20, 'Incomplete'), (-15, 'Imported'), (-10, 'Inactive'), (0, 'New'), (10, 'Active')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('season', models.IntegerField(choices=[(1, 'Summer'), (2, 'Midwinter'), (3, 'Fall'), (4, 'Spring')])),
                ('panel', models.IntegerField(blank=True, choices=[(1, 'Single'), (2, 'Double'), (3, 'Triple'), (4, 'Quadruple'), (5, 'Quintiple')], null=True)),
                ('year', models.IntegerField(choices=[(2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939)])),
                ('open_date', models.DateField(blank=True, null=True)),
                ('close_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(help_text='\n            The location in the form "City, State".', max_length=255)),
                ('timezone', timezone_field.fields.TimeZoneField(help_text='\n            The local timezone of the convention.')),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.fields.ImageUploadPath())),
                ('description', models.TextField(blank=True, help_text='\n            A general description field; usually used for hotel and venue info.', max_length=1000)),
                ('divisions', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(choices=[('EVG', [(10, 'EVG Division I'), (20, 'EVG Division II'), (30, 'EVG Division III'), (40, 'EVG Division IV'), (50, 'EVG Division V')]), ('FWD', [(60, 'FWD Arizona'), (70, 'FWD Northeast'), (80, 'FWD Northwest'), (90, 'FWD Southeast'), (100, 'FWD Southwest')]), ('LOL', [(110, 'LOL 10000 Lakes'), (120, 'LOL Division One'), (130, 'LOL Northern Plains'), (140, 'LOL Packerland'), (150, 'LOL Southwest')]), ('MAD', [(170, 'MAD Central'), (180, 'MAD Northern'), (190, 'MAD Southern')]), ('NED', [(210, 'NED Granite and Pine'), (220, 'NED Mountain'), (230, 'NED Patriot'), (240, 'NED Sunrise'), (250, 'NED Yankee')]), ('SWD', [(260, 'SWD Northeast'), (270, 'SWD Northwest'), (280, 'SWD Southeast'), (290, 'SWD Southwest')])]), blank=True, default=list, size=None)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conventions', to='bhs.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'New'), (2, 'Built'), (5, 'Invited'), (7, 'Withdrawn'), (10, 'Submitted'), (20, 'Approved')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('is_evaluation', models.BooleanField(default=True, help_text='\n            Entry requests evaluation.')),
                ('is_private', models.BooleanField(default=False, help_text='\n            Keep scores private.')),
                ('is_mt', models.BooleanField(default=False, help_text='\n            Keep scores private.')),
                ('draw', models.IntegerField(blank=True, help_text='\n            The draw for the initial round only.', null=True)),
                ('seed', models.IntegerField(blank=True, help_text='\n            The incoming rank based on prelim score.', null=True)),
                ('prelim', models.FloatField(blank=True, help_text='\n            The incoming prelim score.', null=True)),
                ('base', models.FloatField(blank=True, help_text='\n            The incoming base score used to determine most-improved winners.', null=True)),
                ('participants', models.CharField(blank=True, default='', max_length=255)),
                ('pos', models.IntegerField(blank=True, help_text='Estimated Participants-on-Stage', null=True)),
                ('representing', models.CharField(blank=True, default='', max_length=255)),
                ('description', models.TextField(blank=True, help_text='\n            Public Notes (usually from group).', max_length=1000)),
                ('notes', models.TextField(blank=True, help_text='\n            Private Notes (for internal use only).')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='bhs.Group')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
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
                ('legacy_num', models.IntegerField(blank=True, null=True)),
                ('legacy_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcomes', to='api.Award')),
            ],
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
                ('psa', models.FileField(blank=True, default='', upload_to=api.fields.FileUploadPath())),
                ('legacy_num', models.IntegerField(blank=True, null=True)),
                ('legacy_name', models.CharField(blank=True, max_length=255, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panelists', to='bhs.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'New'), (10, 'Built'), (20, 'Started'), (25, 'Finished'), (27, 'Verified'), (30, 'Published')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('kind', models.IntegerField(choices=[(1, 'Finals'), (2, 'Semi-Finals'), (3, 'Quarter-Finals')])),
                ('num', models.IntegerField(default=0)),
                ('spots', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('footnotes', models.TextField(blank=True, help_text='\n            Freeform text field; will print on OSS.')),
                ('oss', models.FileField(blank=True, default='', upload_to=api.fields.FileUploadPath())),
                ('legacy_oss', models.FileField(blank=True, default='', upload_to=api.fields.FileUploadPath())),
                ('sa', models.FileField(blank=True, default='', upload_to=api.fields.FileUploadPath())),
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
                ('legacy_panelist', models.CharField(blank=True, max_length=255, null=True)),
                ('panelist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='api.Panelist')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'New'), (2, 'Built'), (4, 'Opened'), (8, 'Closed'), (10, 'Verified'), (20, 'Packaged'), (30, 'Finished')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('kind', models.IntegerField(choices=[(32, 'Chorus'), (41, 'Quartet'), (42, 'Mixed'), (43, 'Senior'), (44, 'Youth'), (45, 'Unknown'), (46, 'VLQ')], help_text='\n            The kind of session.  Generally this will be either quartet or chorus.\n        ')),
                ('num_rounds', models.IntegerField(default=0)),
                ('is_invitational', models.BooleanField(default=False, help_text='Invite-only (v. Open).')),
                ('description', models.TextField(blank=True, help_text='\n            The Public Description.  Will be sent in all email communications.', max_length=1000)),
                ('notes', models.TextField(blank=True, help_text='\n            Private Notes (for internal use only).  Will not be sent.')),
                ('footnotes', models.TextField(blank=True, help_text='\n            Freeform text field; will print on OSS.')),
                ('legacy_report', models.FileField(blank=True, default='', storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to=api.fields.FileUploadPath())),
                ('drcj_report', models.FileField(blank=True, default='', storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to=api.fields.FileUploadPath())),
                ('convention', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='api.Convention')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'New'), (10, 'Verified'), (38, 'Finished'), (40, 'Confirmed'), (50, 'Final'), (90, 'Announced'), (95, 'Archived')], default=0, help_text='DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.')),
                ('num', models.IntegerField()),
                ('legacy_num', models.IntegerField(blank=True, null=True)),
                ('legacy_chart', models.CharField(blank=True, max_length=255, null=True)),
                ('legacy_total', models.IntegerField(blank=True, null=True)),
                ('asterisks', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None)),
                ('dixons', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None)),
                ('penalties', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(choices=[(10, 'Primarily Patriotic/Religious Intent'), (30, 'Instrumental Accompaniment'), (40, 'Chorus Exceeding 4-Part Texture'), (50, 'Sound Equipment or Electronic Enhancement')]), blank=True, default=list, size=None)),
                ('stats', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('appearance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='api.Appearance')),
                ('chart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', to='bhs.Chart')),
            ],
            options={
                'get_latest_by': ['num'],
            },
        ),
        migrations.AddField(
            model_name='score',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='api.Song'),
        ),
        migrations.AddField(
            model_name='round',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rounds', to='api.Session'),
        ),
        migrations.AddField(
            model_name='panelist',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panelists', to='api.Round'),
        ),
        migrations.AddField(
            model_name='outcome',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcomes', to='api.Round'),
        ),
        migrations.AddField(
            model_name='entry',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='api.Session'),
        ),
    ]
