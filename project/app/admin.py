# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group as AuthGroup

# Local
from .forms import (
    UserChangeForm,
    UserCreationForm,
)

from .inlines import (
    AwardInline,
    AssignmentInline,
    ContestantInline,
    ContestInline,
    HostInline,
    OfficerInline,
    PerformanceInline,
    PerformerInline,
    RoundInline,
    ScoreInline,
    SessionInline,
    SubmissionInline,
)

from .models import (
    Assignment,
    Award,
    Catalog,
    Contest,
    ContestPrivate,
    Contestant,
    ContestantPrivate,
    Convention,
    Entity,
    Host,
    Office,
    Officer,
    Membership,
    Performance,
    PerformancePrivate,
    Performer,
    PerformerPrivate,
    Person,
    Round,
    Score,
    Session,
    Slot,
    Song,
    SongPrivate,
    Submission,
    User,
    Venue,
)


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = [
        'status',
        'kind',
        'convention',
        'person',
    ]

    list_display = [
        'nomen',
        'status',
        'kind',
        'person',
        'convention',
    ]

    list_filter = (
        'status',
        'kind',
    )

    list_select_related = [
        'convention',
        'person',
    ]

    search_fields = [
        'nomen',
    ]

    raw_id_fields = (
        'convention',
        'person',
    )

    readonly_fields = [
        'nomen',
    ]


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):

    fields = [
        'name',
        'status',
        'is_manual',
        'kind',
        'championship_season',
        'qualifier_season',
        'size',
        'size_range',
        'scope',
        'scope_range',
        ('is_primary', 'is_improved', 'is_novice'),
        ('is_multi',),
        'championship_rounds',
        'qualifier_rounds',
        'threshold',
        'minimum',
        'advance',
    ]

    list_display = [
        'nomen',
        'status',
        'is_primary',
        'is_manual',
        'kind',
        'size',
        'size_range',
        'scope',
        'scope_range',
        'is_improved',
        'is_novice',
        'championship_season',
        'qualifier_season',
    ]

    list_filter = [
        'status',
        'is_primary',
        'kind',
        'championship_season',
        'qualifier_season',
        'size',
        'scope',
        'is_manual',
        'is_novice',
        'is_improved',
    ]

    readonly_fields = [
        'nomen',
    ]

    search_fields = [
        'nomen',
    ]

    ordering = (
        'kind',
        '-is_primary',
        'is_improved',
        'size',
        'scope',
        'is_novice',
    )


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):

    fields = [
        'nomen',
        'status',
        'bhs_id',
        'title',
        'published',
        'arranger',
        'arranger_fee',
        'difficulty',
        'gender',
        'tempo',
        'is_medley',
        'is_learning',
        'voicing',
    ]

    list_display = [
        'nomen',
        'status',
        'title',
        'arranger',
    ]

    list_editable = [
        'title',
        'arranger',
    ]

    list_filter = [
        'status',
    ]

    # inlines = [
    #     SubmissionInline,
    # ]

    readonly_fields = [
        'nomen',
    ]

    search_fields = [
        'nomen',
    ]

    ordering = (
        'nomen',
    )


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    fields = [
        'status',
        'award',
        'session',
        'is_qualifier',
    ]

    list_display = (
        'nomen',
        'session',
    )

    list_filter = [
        'status',
        'award__kind',
        'award__is_primary',
        'is_qualifier',
    ]

    save_on_top = True

    inlines = [
        ContestantInline,
    ]

    readonly_fields = [
        'nomen',
    ]

    raw_id_fields = [
        'award',
        'session',
    ]

    search_fields = [
        'nomen',
    ]


@admin.register(ContestPrivate)
class ContestPrivateAdmin(admin.ModelAdmin):
    pass


@admin.register(Contestant)
class ContestantAdmin(admin.ModelAdmin):

    fields = [
        'status',
        'performer',
        'contest',
    ]

    list_filter = (
        'status',
    )

    readonly_fields = [
        'nomen',
    ]

    raw_id_fields = [
        'performer',
        'contest',
    ]

    search_fields = [
        'nomen',
    ]

    ordering = (
        'nomen',
    )


@admin.register(ContestantPrivate)
class ContestantPrivateAdmin(admin.ModelAdmin):
    pass


@admin.register(Convention)
class ConventionAdmin(admin.ModelAdmin):

    fields = (
        'name',
        'status',
        'entity',
        'level',
        'venue',
        'risers',
        'start_date',
        'end_date',
        'year',
        'season',
    )

    list_display = (
        'nomen',
        'name',
        'panel',
        'season',
        # 'status',
        'start_date',
        'end_date',
        'level',
        # 'venue',
    )

    list_filter = (
        'status',
        'level',
        'season',
        'year',
    )

    fsm_field = [
        'status',
    ]

    search_fields = (
        'nomen',
    )

    inlines = [
        AssignmentInline,
        HostInline,
        SessionInline,
    ]

    readonly_fields = (
        'nomen',
    )

    raw_id_fields = [
        'entity',
        'venue',
    ]

    ordering = (
        '-year',
        'level',
    )

    save_on_top = True


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'status',
        'parent',
        'kind',
        'code',
        'start_date',
        'end_date',
        'short_name',
        'long_name',
        'location',
        # 'representative',
        # 'spots',
        'website',
        'facebook',
        'twitter',
        'email',
        'phone',
        'picture',
        'description',
        'notes',
    ]

    list_filter = [
        'status',
        'kind',
    ]

    search_fields = [
        'nomen',
    ]

    list_display = [
        'nomen',
        'status',
        'code',
        'short_name',
        'long_name',
        'kind',
    ]

    inlines = [
        AwardInline,
        # OrganizationInline,
    ]

    readonly_fields = [
        'nomen',
    ]

    raw_id_fields = [
        'parent',
    ]

    ordering = [
        'kind',
        'name',
    ]


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    fields = [
        'status',
        'convention',
    ]

    list_display = [
        'nomen',
        'status',
        'convention',
    ]

    list_filter = [
        'status',
    ]

    raw_id_fields = [
        'convention',
    ]

    ordering = (
        'nomen',
    )

    search_fields = [
        'nomen',
    ]

    readonly_fields = [
        'nomen',
    ]


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    fields = [
        'status',
        'start_date',
        'end_date',
        'entity',
        'person',
    ]
    list_display = [
        'status',
        'start_date',
        'end_date',
        'entity',
        'person',
    ]
    raw_id_fields = [
        'person',
        'entity',
    ]
    search_fields = [
        'nomen',
    ]
    list_filter = [
        'status',
        'part',
        'entity__kind',
    ]
    inlines = [
        OfficerInline,
    ]


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'short_name',
        'kind',
    ]
    search_fields = [
        'nomen',
        'short_name',
    ]

    list_filter = [
        'status',
        'kind',
    ]


@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    raw_id_fields = [
        'office',
        'membership',
    ]
    list_display = [
        'membership',
        'office',
    ]
    list_filter = [
        'office__name',
    ]
    search_fields = [
        'nomen',
    ]


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    fields = [
        # 'name',
        'status',
        'actual_start',
        'actual_finish',
        'performer',
        'round',
        'num',
        'slot',
    ]

    list_display = [
        'nomen',
        'status',
    ]

    list_filter = [
        'status',
        'round__session__kind',
        'round__session__convention__season',
        'round__session__convention__year',
        # 'round__session__convention__organization',
    ]

    fsm_field = [
        'status',
    ]

    save_on_top = True

    readonly_fields = [
        'nomen',
    ]

    raw_id_fields = (
        'performer',
    )

    search_fields = (
        'nomen',
    )

    inlines = [
        # SongInline,
    ]


@admin.register(PerformancePrivate)
class PerformancePrivateAdmin(admin.ModelAdmin):
    pass


@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    fields = (
        # 'name',
        'status',
        'bhs_id',
        'picture',
        # 'csa_pdf',
        'session',
        # 'group',
        # 'district',
        # 'division',
        'risers',
        ('is_evaluation', 'is_private',),
        ('tenor', 'lead', 'baritone', 'bass',),
        ('director', 'codirector', 'men'),
        'prelim',
        'seed',
    )

    list_display = (
        'nomen',
        'status',
    )

    list_filter = [
        'status',
        'session__convention__level',
        'session__kind',
        'session__convention__season',
        # 'session__convention__organization',
        'session__convention__year',
        'risers',
    ]

    fsm_field = [
        'status',
    ]

    inlines = [
        PerformanceInline,
        ContestantInline,
        SubmissionInline,
    ]

    search_fields = (
        'nomen',
    )

    raw_id_fields = (
        'session',
        # 'group',
        'tenor',
        'lead',
        'baritone',
        'bass',
        'director',
        'codirector',
    )

    readonly_fields = (
        'nomen',
    )

    save_on_top = True

    ordering = (
        'nomen',
    )


@admin.register(PerformerPrivate)
class PerformerPrivateAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = (
        'name',
        # 'common_name',
        'status',
        'kind',
        'birth_date',
        'start_date',
        'end_date',
        'dues_thru',
        'mon',
        'spouse',
        'location',
        'website',
        'facebook',
        'twitter',
        'email',
        'phone',
        'bhs_id',
        'picture',
        'description',
        'notes',
    )

    list_display = (
        'nomen',
        'status',
        'bhs_id',
        'location',
        'website',
        'facebook',
        'twitter',
        'picture',
    )

    list_filter = [
        'status',
    ]

    readonly_fields = [
        'nomen',
    ]

    # inlines = [
    #     RoleInline,
    #     MemberInline,
    #     JudgeInline,
    # ]

    search_fields = (
        'nomen',
    )

    save_on_top = True

    # readonly_fields = [
    #     'common_name',
    # ]


@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
    fields = [
        # 'name',
        'status',
        ('session', 'kind',),
        'num_songs',
        # 'mt',
        'start_date',
        'end_date',
        'ann_pdf',
    ]

    list_display = [
        'nomen',
        'status',
    ]

    list_filter = [
        'status',
        'session__kind',
        'session__convention__level',
        'session__convention__season',
        'session__convention__year',
        # 'session__convention__organization',
    ]

    fsm_field = [
        'status',
    ]

    save_on_top = True

    readonly_fields = [
        'nomen',
        # 'session',
        # 'kind',
    ]

    raw_id_fields = (
        'session',
        # 'mt',
    )

    inlines = [
        PerformanceInline,
    ]

    search_fields = [
        'nomen',
    ]


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    fields = [
        # 'name',
        # 'status',
        'song',
        'person',
        'category',
        'kind',
        'original',
        'violation',
        'penalty',
        'points',
    ]

    readonly_fields = [
        'nomen',
        'song',
        'person',
    ]

    list_display = [
        'nomen',
        # 'status',
        'points',
    ]

    # list_filter = [
    #     'status',
    # ]

    raw_id_fields = [
        'song',
        'person',
    ]

    ordering = [
        'song',
        'person',
    ]
    save_on_top = True


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    fsm_field = [
        'status',
    ]

    save_on_top = True
    fields = [
        # 'name',
        'status',
        'convention',
        'kind',
        'num_rounds',
        'panel_size',
        # 'start_date',
        # 'end_date',
        'primary',
        'current',
        # 'cursor',
        # 'year',
        # # 'size',
        'scoresheet_pdf',
    ]

    list_display = [
        'nomen',
        'status',
    ]

    list_filter = (
        'status',
        'kind',
        'convention__level',
        'convention__season',
        'convention__year',
        # 'convention__organization',
    )

    raw_id_fields = (
        'convention',
        'current',
        'primary',
    )

    readonly_fields = [
        'nomen',
    ]

    inlines = [
        RoundInline,
        PerformerInline,
        ContestInline,
    ]

    list_select_related = [
        'convention',
    ]

    ordering = (
        '-convention__year',
        'convention__level',
        # 'convention__organization__name',
        '-convention__season',
        'kind',
    )

    search_fields = [
        'nomen',
    ]


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = [
        # 'name',
        'status',
        'num',
        'onstage',
        'round',
    ]
    list_display = [
        'nomen',
        'status',
        'onstage',
    ]

    list_filter = (
        'status',
    )

    readonly_fields = [
        'nomen',
    ]
    raw_id_fields = [
        'round',
    ]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    fields = [
        # 'name',
        # 'status',
        'performance',
        'submission',
        'num',

        # 'title',
    ]

    list_display = (
        'nomen',
        # 'status',
        # 'title',
        'performance',
        'submission',
        'num',
    )

    # list_filter = (
    #     'status',
    # )

    search_fields = (
        'nomen',
    )

    inlines = [
        ScoreInline,
    ]
    save_on_top = True

    readonly_fields = (
        'nomen',
    )

    raw_id_fields = (
        'performance',
        'submission',
    )

    ordering = (
        'nomen',
        'num',
    )


@admin.register(SongPrivate)
class SongPrivateAdmin(admin.ModelAdmin):
    pass


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = [
        # 'name',
        'status',
        'performer',
        'title',
        'bhs_catalog',
        'arrangers',
        'composers',
        'holders',
        # 'source',
        'is_medley',
        'is_parody',
    ]

    list_display = [
        'nomen',
        'status',
        'title',
        'arrangers',
    ]

    list_filter = (
        'status',
    )

    raw_id_fields = (
        'performer',
    )

    readonly_fields = [
        'nomen',
    ]


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = (
        'name',
        'status',
        'city',
        'state',
        'airport',
        'timezone',
    )

    list_display = [
        'nomen',
        'name',
        'city',
        'state',
        'timezone',
    ]

    list_filter = (
        'status',
    )

    search_fields = (
        'nomen',
    )

    readonly_fields = [
        'nomen',
    ]

    inlines = [
        # ConventionInline,
    ]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'email',
        'person',
        'is_active',
        'is_staff',
    ]

    list_filter = (
        'is_active',
        'is_staff',
    )

    fieldsets = (
        (None, {'fields': ('email', 'is_active', 'is_staff', 'person', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('person', )}),
    )

    search_fields = [
        'email',
    ]
    ordering = ('email',)
    filter_horizontal = ()
    raw_id_fields = [
        'person',
    ]

    readonly_fields = [
        'email',
    ]

admin.site.unregister(AuthGroup)
