# Third-Party
from django_fsm_log.admin import StateLogInline
from fsm_admin.mixins import FSMTransitionMixin

# Django
from django.contrib import admin
from reversion.admin import VersionAdmin
from django.conf import settings

# Local
from .inlines import ContestInline
from .inlines import EntryInline


from .models import Assignment
from .models import Contest
from .models import Entry
from .models import Session



admin.site.site_header = 'Barberscore Admin Backend'


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = [
        'kind',
        'category',
        'person_id',
        'name',
        'first_name',
        'last_name',
        'district',
        'area',
        'email',
        'cell_phone',
        'bhs_id',
        'session',
    ]

    list_display = [
        'name',
        'bhs_id',
        'session',
        'category',
        'kind',
    ]

    list_filter = (
        'kind',
        'category',
        # ActiveConventionListFilter,
    )

    list_select_related = [
        'session',
    ]

    search_fields = [
        'id',
    ]

    autocomplete_fields = [
        'session',
    ]

    readonly_fields = [
    ]

    raw_id_fields = [
        # 'user',
    ]
    ordering = [
        'session',
        'kind',
        'last_name',
        'first_name',
    ]


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'award_id',
        'name',
        'kind',
        'gender',
        'district',
        'division',
        'age',
        'level',
        'season',
        'is_single',
        'is_novice',
        'description',
        'scope',
        'scope_range',
        'size',
        'size_range',
        'tree_sort',
        'session',

    ]

    list_display = (
        'name',
        # 'convention_name',
        'session',
        # 'group',
    )

    list_filter = [
        # 'award__kind',
    ]

    save_on_top = True

    inlines = [
    ]

    readonly_fields = [
        'id',
        'tree_sort',
        # 'convention_name',
    ]

    autocomplete_fields = [
        # 'award',
        'session',
        # 'group',
    ]

    search_fields = [
        'name',
        'district',
    ]
    ordering = [
        # '-session__convention__year',
        # 'session__convention__season',
        # 'session__convention__district',
        # 'session__convention__name',
        'session',
        'name',
    ]


@admin.register(Entry)
class EntryAdmin(VersionAdmin, FSMTransitionMixin):
    fsm_field = [
        'status',
    ]

    fieldsets = (
        (None, {
            'fields': (
                'id',
                'nomen',
                'status',
            ),
        }),
        ('Entry Preferences', {
            'fields': (
                'participants',
                'chapters',
                'pos',
                'is_evaluation',
                'is_private',
                'notes',
            ),
        }),
        ('DRCJ Preferences', {
            'fields': (
                'area',
                'prelim',
                'base',
                'draw',
                'is_mt',
            ),
        }),
        ('Contests', {
            'fields': (
                'contests',
                # 'charts',
                # 'awards',
            ),
            'classes': ('wide',),
        }),
        ('Group Info', {
            'fields': (
                'group_id',
                'name',
                'kind',
                'gender',
                'district',
                'division',
                'bhs_id',
                'code',
                'is_senior',
                'is_youth',
                'image',
                'description',
            ),
            'classes': ('collapse',),
        }),
        ('Misc', {
            'fields': (
                'owners',
                'created',
                'modified',
            ),
        }),
    )

    list_display = (
        '__str__',
        'kind',
        'session',
        'status',
    )

    list_select_related = [
        'session',
    ]

    list_filter = [
        'status',
        'kind',
        'district',
    ]

    inlines = [
        # OwnerInline,
        # ContestInline,
        StateLogInline,
    ]

    search_fields = [
        'id',
        'name',
        'bhs_id',
        'owners__email',
        'owners__name',
        'participants',
        'code',
    ]

    autocomplete_fields = [
        'session',
        'contests',
        'owners',
    ]
    readonly_fields = [
        'id',
        'nomen',
        'created',
        'modified',
        'group_id',
        'name',
        'kind',
        'gender',
        'district',
        'division',
        'bhs_id',
        'code',
        'is_senior',
        'is_youth',
        'image',
        'description',
    ]

    save_on_top = True
    save_on_bottom = True

    ordering = [
        'name',
        'session',
    ]


@admin.register(Session)
class SessionAdmin(VersionAdmin, FSMTransitionMixin):
    fsm_field = [
        'status',
    ]
    save_on_top = True
    fields = [
        'id',
        'status',
        'convention',
        'name',
        'district',
        'divisions',
        ('year', 'season', ),
        'panel',
        'kind',
        ('num_rounds', 'is_invitational',),
        ('open_date', 'close_date', ),
        ('start_date', 'end_date', ),
        'owners',
        'venue_name',
        'location',
        'timezone',
        'image',

        'notes',
        # 'target',
        'legacy_report',
        'drcj_report',
        # 'contests',
        # 'footnotes',
        # 'description',

        # 'name',



    ]

    list_display = [
        # 'id',
        'district',
        # 'convention__district',
        'kind',
        'name',
        # 'num_rounds',
        'is_invitational',
        'status',
    ]

    list_filter = (
        # ConventionStatusListFilter,
        'status',
        'kind',
        'district',
        'num_rounds',
        'is_invitational',
        'season',
        # 'year',
    )

    autocomplete_fields = [
        # 'convention',
        # 'target',
        'owners',
    ]

    readonly_fields = [
        'id',
        # 'legacy_report',
        # 'drcj_report',
    ]

    inlines = [
        # RoundInline,
        ContestInline,
        EntryInline,
        StateLogInline,
    ]

    list_select_related = [
        # 'convention',
    ]

    ordering = [
        'district',
        'kind',
        'name',
        # 'convention__group__tree_sort',
    ]

    search_fields = [
        'district',
        'kind',
    ]

    # raw_id_fields = [
    #     'owners',
    # ]

    class Media:
        js = ('registration/js/admin/convention_change.js',)

    def save_model(self, request, obj, form, change):
        if not obj.image:
            if settings.DISTRICT_DEFAULT_LOGOS[obj.district]:
                obj.image = settings.DISTRICT_DEFAULT_LOGOS[obj.district]
        super().save_model(request, obj, form, change)
