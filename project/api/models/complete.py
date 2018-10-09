from django.db import models
import uuid
from model_utils import Choices

class Complete(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    row = models.IntegerField(
        null=True,
        blank=True,
    )

    year = models.IntegerField(
        null=True,
        blank=True,
    )

    district = models.CharField(
        blank=True,
        max_length=255,
    )

    name = models.CharField(
        blank=True,
        max_length=255,
    )

    SEASON = Choices(
        (1, 'summer', 'Summer',),
        (2, 'midwinter', 'Midwinter',),
        (3, 'fall', 'Fall',),
        (4, 'spring', 'Spring',),
        (9, 'video', 'Video',),
    )

    season = models.IntegerField(
        null=True,
        blank=True,
        choices=SEASON
    )

    SESSION_KIND = Choices(
        (32, 'chorus', "Chorus"),
        (41, 'quartet', "Quartet"),
        (42, 'mixed', "Mixed"),
    )

    session_kind = models.IntegerField(
        null=True,
        blank=True,
        choices=SESSION_KIND
    )

    ROUND_KIND = Choices(
        (1, 'finals', 'Finals'),
        (2, 'semis', 'Semi-Finals'),
        (3, 'quarters', 'Quarter-Finals'),
    )

    round_kind = models.IntegerField(
        null=True,
        blank=True,
        choices=ROUND_KIND
    )

    CATEGORY = Choices(
        (30, 'music', 'Music'),
        (40, 'performance', 'Performance'),
        (50, 'singing', 'Singing'),
    )

    category = models.IntegerField(
        null=True,
        blank=True,
        choices=CATEGORY
    )

    judge = models.CharField(
        blank=True,
        max_length=255,
    )

    single = models.CharField(
        blank=True,
        max_length=255,
    )

    draw = models.IntegerField(
        null=True,
        blank=True,
    )

    num = models.IntegerField(
        null=True,
        blank=True,
    )

    panelist_num = models.IntegerField(
        null=True,
        blank=True,
    )

    group_name = models.CharField(
        blank=True,
        max_length=255,
    )

    song_title = models.CharField(
        blank=True,
        max_length=255,
    )

    points = models.IntegerField(
        null=True,
        blank=True,
    )

    convention = models.ForeignKey(
        'Convention',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    session = models.ForeignKey(
        'Session',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    competitor = models.ForeignKey(
        'Competitor',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    round = models.ForeignKey(
        'Round',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panelist = models.ForeignKey(
        'Panelist',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    appearance = models.ForeignKey(
        'Appearance',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    song = models.ForeignKey(
        'Song',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    score = models.ForeignKey(
        'Score',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )