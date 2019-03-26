
# Standard Library
import logging
import uuid
import pydf

# Third-Party
from django_fsm_log.models import StateLog
from dry_rest_permissions.generics import allow_staff_or_superuser
from dry_rest_permissions.generics import authenticated_users
from model_utils import Choices
from model_utils.models import TimeStampedModel

# Django
from django.apps import apps
from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.functional import cached_property
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django.db.models import Avg, StdDev, Q


import django_rq
from api.tasks import send_email


log = logging.getLogger(__name__)


class Panelist(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    STATUS = Choices(
        (-10, 'inactive', 'Inactive',),
        (0, 'new', 'New',),
        (10, 'active', 'Active',),
    )

    status = models.IntegerField(
        choices=STATUS,
        default=STATUS.new,
    )

    num = models.IntegerField(
        blank=True,
        null=True,
    )

    KIND = Choices(
        (10, 'official', 'Official'),
        (20, 'practice', 'Practice'),
        (30, 'observer', 'Observer'),
    )

    kind = models.IntegerField(
        choices=KIND,
    )

    CATEGORY = Choices(
        (5, 'drcj', 'DRCJ'),
        (10, 'ca', 'CA'),
        (30, 'music', 'Music'),
        (40, 'performance', 'Performance'),
        (50, 'singing', 'Singing'),
    )

    category = models.IntegerField(
        choices=CATEGORY,
        null=True,
        blank=True,
    )

    legacy_num = models.IntegerField(
        null=True,
        blank=True,
    )

    legacy_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    # FKs
    round = models.ForeignKey(
        'Round',
        related_name='panelists',
        on_delete=models.CASCADE,
    )

    person = models.ForeignKey(
        'Person',
        related_name='panelists',
        on_delete=models.CASCADE,
    )

    # Relations
    statelogs = GenericRelation(
        StateLog,
        related_query_name='panelists',
    )

    @cached_property
    def row_class(self):
        if self.category == self.CATEGORY.music:
            row_class = 'warning'
        elif self.category == self.CATEGORY.performance:
            row_class = 'success'
        elif self.category == self.CATEGORY.singing:
            row_class = 'info'
        else:
            row_class = None
        return row_class


    # Internals
    class Meta:
        unique_together = (
            ('round', 'num',),
            ('round', 'person', 'category',),
        )

    class JSONAPIMeta:
        resource_name = "panelist"

    def __str__(self):
        return "{0} {1}".format(
            self.round,
            self.num,
        )

    def clean(self):
        if self.kind > self.KIND.practice:
            raise ValidationError(
                {'category': 'Panel may only contain Official and Practice'}
            )
        if self.num and self.num > 50 and self.kind == self.KIND.official:
            raise ValidationError(
                {'num': 'Official Num must be less than 50'}
            )
        if self.num and self.num <= 50 and self.kind == self.KIND.practice:
            raise ValidationError(
                {'num': 'Practice Num must be greater than 50'}
            )
        if self.num and self.num and self.category == self.CATEGORY.ca:
            raise ValidationError(
                {'num': 'CAs must not have a num.'}
            )

    # Permissions
    @staticmethod
    @allow_staff_or_superuser
    @authenticated_users
    def has_read_permission(request):
        return True

    @allow_staff_or_superuser
    @authenticated_users
    def has_object_read_permission(self, request):
        return True

    @staticmethod
    @allow_staff_or_superuser
    @authenticated_users
    def has_write_permission(request):
        return any([
            request.user.is_round_manager,
        ])

    @allow_staff_or_superuser
    @authenticated_users
    def has_object_write_permission(self, request):
        return any([
            all([
                self.round.session.convention.assignments.filter(
                    person__user=request.user,
                    status__gt=0,
                    category__lte=10,
                ),
                self.round.status < self.round.STATUS.started,
            ]),
        ])

    def get_jsa(self):

        appearances = self.round.appearances.prefetch_related(
            'songs',
        ).order_by(
            '-num',
        )

        # Monkeypatching
        class_map = {
            Panelist.CATEGORY.music: 'badge badge-warning mono-font',
            Panelist.CATEGORY.performance: 'badge badge-success mono-font',
            Panelist.CATEGORY.singing: 'badge badge-info mono-font',
        }
        for appearance in appearances:
            songs = appearance.songs.order_by(
                'num',
            ).annotate(
                avg=Avg(
                    'scores__points',
                    filter=Q(
                        scores__panelist__kind=Panelist.KIND.official,
                    ),
                ),
                dev=StdDev(
                    'scores__points',
                    filter=Q(
                        scores__panelist__kind=Panelist.KIND.official,
                    ),
                ),
            )
            appearance.songs_patched = songs
            for song in songs:
                scores = song.scores.filter(
                    panelist__kind=Panelist.KIND.official,
                ).order_by('points')
                out = []
                for score in scores:
                    if score.points == 0:
                        score.points = "00"
                    span_class = class_map[score.panelist.category]
                    if score.panelist == self:
                        span_class = "{0} black-font".format(span_class)
                    out.append((score.points, span_class))
                song.scores_patched = out

        context = {
            'panelist': self,
            'appearances': appearances,
        }
        rendered = render_to_string('reports/jsa.html', context)
        file = pydf.generate_pdf(rendered)
        content = ContentFile(file)
        return content

    def save_jsa(self):
        content = self.get_jsa()
        self.refresh_from_db()
        self.jsa.save(
            "{0}-jsa".format(
                slugify(self.person.name),
            ),
            content,
        )
