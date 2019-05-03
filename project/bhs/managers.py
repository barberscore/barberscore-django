from datetime import date

# Third-Party
import django_rq
from django_fsm_log.models import StateLog

# Django
from django.apps import apps
from django.db.models import Manager
from django.db.models import Q
from django.db.models import F
from django.db.models import Min
from django.db.models import Max
from django.db.models import When
from django.db.models import Subquery
from django.db.models import OuterRef
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import DateField
from django.db.models import Case

from .tasks import get_accounts


class HumanManager(Manager):
    def export_values(self, cursor=None):
        hs = self.filter(
            Q(merged_id="") | Q(merged_id=None),
            Q(deleted_id="") | Q(deleted_id=None),
        )
        if cursor:
            hs = hs.filter(
                modified__gte=cursor,
            )
        return list(hs.values(
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'nick_name',
            'email',
            'birth_date',
            'home_phone',
            'cell_phone',
            'work_phone',
            'bhs_id',
            'gender',
            'part',
            'mon',
            'is_deceased',
            'is_honorary',
            'is_suspended',
            'is_expelled',
        ))

    # def update_persons(self, cursor=None):
    #     # Get base
    #     humans = self.all()
    #     # Filter if cursored
    #     if cursor:
    #         humans = self.filter(
    #             modified__gt=cursor,
    #         )
    #     else:
    #         # Else clear logs
    #         ss = StateLog.objects.filter(
    #             content_type__model='person',
    #             groups__mc_pk__isnull=False,
    #         )
    #         ss.delete()
    #     t = humans.count()
    #     # Creating/Update Persons
    #     Person = apps.get_model('api.person')
    #     queue = django_rq.get_queue('low')
    #     for human in humans:
    #         queue.enqueue(
    #             Person.objects.update_or_create_from_human,
    #             human,
    #         )
    #     return t

    def delete_orphans(self):
        # Get base
        humans = list(self.values_list('id', flat=True))
        # Delete Orphans
        Person = apps.get_model('api.person')
        orphans = Person.objects.filter(
            mc_pk__isnull=False,
        ).exclude(
            mc_pk__in=humans,
        )
        t = orphans.count()
        orphans.delete()
        return t


    def get_account_orphans(self):
        # Get humans
        humans = list(self.values_list('id', flat=True))
        # Get accounts
        accounts = get_accounts()
        mc_pks = [x['app_metadata']['mc_pk'] for x in accounts]
        # Get orphans
        orphans = [{'id': item} for item in mc_pks if item not in humans]
        return orphans


    def get_account_adoptions(self):
        # Get accounts
        accounts = get_accounts()
        mc_pks = [x['app_metadata']['mc_pk'] for x in accounts]
        # Get current
        human_values = list(self.values(
            'id',
            'first_name',
            'last_name',
            'nick_name',
            'email',
            'bhs_id',
        ))
        # Rebuild list for verified emails only.
        # Can skip this part if we trust MC data (which we don't currently)
        humans = [x for x in human_values if x['email']]
        # Get adoptions
        adoptions = [item for item in humans if item['id'] not in mc_pks]
        return adoptions


class StructureManager(Manager):
    def export_values(self, cursor=None):
        output = []
        types = [
            'organization',
            'district',
            'group',
            'chapter',
            'chorus',
            'quartet',
        ]
        for t in types:
            ss = self.filter(
                Q(kind=t),
                Q(deleted_id="") | Q(deleted_id=None),
            )
            if cursor:
                ss = ss.filter(
                    modified__gte=cursor,
                )
            output.extend(
                list(ss.values(
                    'id',
                    'name',
                    'kind',
                    'gender',
                    'division',
                    'bhs_id',
                    'chapter_code',
                    'website',
                    'email',
                    'phone',
                    'fax',
                    'facebook',
                    'twitter',
                    'youtube',
                    'pinterest',
                    'flickr',
                    'instagram',
                    'soundcloud',
                    'preferred_name',
                    'visitor_information',
                    'established_date',
                    'status_id',
                    'parent_id',
                ))
            )
        return output


    # def update_groups(self, cursor=None):
    #     # Get base
    #     structures = self.select_related('parent').all()
    #     if cursor:
    #         # Filter if cursored
    #         structures = structures.filter(
    #             modified__gt=cursor,
    #         )
    #     else:
    #         # Else clear logs
    #         ss = StateLog.objects.filter(
    #             content_type__model='group',
    #             groups__mc_pk__isnull=False,
    #         )
    #         ss.delete()
    #     t = structures.count()
    #     # Creating/Update Groups
    #     Group = apps.get_model('api.group')
    #     queue = django_rq.get_queue('low')
    #     for structure in structures:
    #         queue.enqueue(
    #             Group.objects.update_or_create_from_structure,
    #             structure,
    #         )
    #     return t

    def delete_orphans(self):
        # Get base
        structures = list(self.values_list('id', flat=True))
        # Delete Orphans
        Group = apps.get_model('api.group')
        orphans = Group.objects.filter(
            mc_pk__isnull=False,
        ).exclude(
            mc_pk__in=structures,
        )
        t = orphans.count()
        orphans.delete()
        return t


class JoinManager(Manager):
    def export_values(self, cursor=None):
        Structure = apps.get_model('bhs.structure')
        today = date.today()
        js = self.select_related(
            'structure',
            'membership',
            'subscription',
            'subscription__human',
        ).filter(
            Q(paid=True),
            Q(deleted__isnull=True),
            Q(membership__deleted_id="") | Q(membership__deleted_id=None),
            Q(subscription__deleted=None),
            Q(structure__deleted_id="") | Q(structure__deleted_id=None),
            Q(subscription__human__merged_id="") | Q(subscription__human__merged_id=None),
            Q(subscription__human__deleted_id="") | Q(subscription__human__deleted_id=None),
        )
        if cursor:
            js = js.filter(
                Q(modified__gte=cursor) |
                Q(membership__modified__gte=cursor) |
                Q(subscription__modified__gte=cursor)
            )
        js = js.values(
            'structure__id',
            'subscription__human__id',
        )
        js = js.annotate(
            id=Max('id'),
            vocal_part=Subquery(
                self.filter(
                    structure__id=OuterRef('structure__id'),
                    subscription__human__id=OuterRef('subscription__human__id'),
                ).order_by(
                    '-modified',
                ).values('part')[:1],
                output_field=CharField()
            ),
            inactivist_date=Subquery(
                self.filter(
                    structure__id=OuterRef('structure__id'),
                    subscription__human__id=OuterRef('subscription__human__id'),
                ).order_by(
                    F('inactive_date').desc(nulls_first=True)
                ).values('inactive_date')[:1],
                output_field=DateField()
            ),
            currentest_date=Subquery(
                self.filter(
                    structure__id=OuterRef('structure__id'),
                    subscription__human__id=OuterRef('subscription__human__id'),
                ).order_by(
                    F('subscription__current_through').desc(nulls_first=True)
                ).values('subscription__current_through')[:1],
                output_field=DateField()
            ),
            startest_date=Min('established_date'),
            endest_date=Case(
                When(
                    Q(
                        structure__kind__in=[
                            Structure.KIND.chorus,
                            Structure.KIND.chapter,
                        ],
                    ),
                    then=F('inactivist_date'),
                ),
                default=F('currentest_date'),
                output_field=DateField(),
            ),
            status=Case(
                When(endest_date__isnull=True, then=10),
                When(endest_date__gte=today, then=10),
                default=-10,
                output_field=IntegerField(),
            ),
        ).values(
            'structure__id',
            'subscription__human__id',
            'id',
            'vocal_part',
            'startest_date',
            'endest_date',
            'status',
        )
        return list(js)


    # def update_members(self, cursor=None):
    #     # Get all records as values
    #     joins = self.filter(
    #         paid=True,
    #         deleted__isnull=True,
    #     ).select_related(
    #         'structure',
    #         'subscription',
    #         'subscription__human',
    #     )
    #     if cursor:
    #         joins = joins.filter(
    #             modified__gt=cursor,
    #         )
    #     t = joins.count()
    #     # Creates race condition on multi-worker
    #     Member = apps.get_model('api.member')
    #     queue = django_rq.get_queue('low')
    #     for join in joins:
    #         queue.enqueue(
    #             Member.objects.update_or_create_from_join,
    #             join,
    #         )
    #     return t

    def delete_orphans(self):
        # Get base
        joins = list(self.values_list('id', flat=True))
        # Delete Orphans
        Member = apps.get_model('api.member')
        orphans = Member.objects.filter(
            mc_pk__isnull=False,
        ).exclude(
            mc_pk__in=joins,
        )
        t = orphans.count()
        orphans.delete()
        return t


class RoleManager(Manager):
    def export_values(self, cursor=None):
        today = date.today()
        rs = self.filter(
            Q(structure__deleted_id="") | Q(structure__deleted_id=None),
            Q(human__merged_id="") | Q(human__merged_id=None),
            Q(human__deleted_id="") | Q(human__deleted_id=None),
        )
        if cursor:
            rs = rs.filter(
                modified__gte=cursor,
            )
        return list(rs.values(
            'name',
            'human_id',
            'structure_id',
        ).annotate(
            id=Max('id'),
            startest_date=Min('start_date'),
            endest_date=Max('end_date'),
            status=Case(
                When(endest_date=None, then=10),
                When(endest_date__gte=today, then=10),
                default=-10,
                output_field=IntegerField(),
            ),
        ))

    # def update_officers(self, cursor=None):
    #     roles = self.select_related(
    #         'structure',
    #         'human',
    #     )
    #     if cursor:
    #         roles = roles.filter(
    #             modified__gt=cursor,
    #         )
    #     t = roles.count()
    #     # Creates race condition on multi-worker
    #     Officer = apps.get_model('api.officer')
    #     queue = django_rq.get_queue('low')
    #     for role in roles:
    #         queue.enqueue(
    #             Officer.objects.update_or_create_from_role,
    #             role,
    #         )
    #     return t

    def delete_orphans(self):
        # Get base
        roles = list(self.values_list('id', flat=True))
        # Delete Orphans
        Officer = apps.get_model('api.officer')
        orphans = Officer.objects.filter(
            mc_pk__isnull=False,
        ).exclude(
            mc_pk__in=roles,
        )
        t = orphans.count()
        orphans.delete()
        return t
