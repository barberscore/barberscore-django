


# Standard Library
import datetime

# Third-Party
from factory import Faker  # post_generation,
from factory import Iterator
from factory import LazyAttribute
from factory import PostGenerationMethodCall
from factory import RelatedFactory
from factory import Sequence
from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.django import mute_signals
from factory.fuzzy import FuzzyInteger

# Django
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.db.models.signals import pre_save

# First-Party
from api.models import Appearance
from api.models import Assignment
from api.models import Award
from api.models import Chart
from api.models import Contest
from api.models import Contender
from api.models import Contestant
from api.models import Convention
from api.models import Entry
from api.models import Group
from api.models import Member
from api.models import Office
from api.models import Officer
from api.models import Outcome
from api.models import Panelist
from api.models import Person
from api.models import Repertory
from api.models import Round
from api.models import Score
from api.models import Session
from api.models import Song
from api.models import User

from stage.models import Grid
from stage.models import Venue


class AppearanceFactory(DjangoModelFactory):
    status = Appearance.STATUS.new
    num = 1
    actual_start = None
    actual_finish = None
    round = SubFactory('factories.RoundFactory')
    group = SubFactory('factories.GroupFactory')

    class Meta:
        model = Appearance


class AssignmentFactory(DjangoModelFactory):
    status = Assignment.STATUS.active
    kind = Assignment.KIND.official
    convention = SubFactory('factories.ConventionFactory')
    person = SubFactory('factories.PersonFactory')

    class Meta:
        model = Assignment


class AwardFactory(DjangoModelFactory):
    name = Faker('word')
    status = Award.STATUS.active
    kind = Award.KIND.quartet
    level = Award.LEVEL.championship
    season = Award.SEASON.summer
    is_single = False
    threshold = None
    minimum = None
    advance = None
    group = SubFactory('factories.GroupFactory')

    class Meta:
        model = Award


class ChartFactory(DjangoModelFactory):
    status = Chart.STATUS.active
    title = Faker('word')
    arrangers = Faker('name_male')
    composers = Faker('name_male')
    lyricists = Faker('name_male')

    class Meta:
        model = Chart


class ContestFactory(DjangoModelFactory):
    status = Contest.STATUS.included
    session = SubFactory('factories.SessionFactory')
    award = SubFactory('factories.AwardFactory')

    class Meta:
        model = Contest


class ContestantFactory(DjangoModelFactory):
    status = Contestant.STATUS.new
    entry = SubFactory('factories.EntryFactory')
    contest = SubFactory('factories.ContestFactory')

    class Meta:
        model = Contestant


class ContenderFactory(DjangoModelFactory):
    status = Contender.STATUS.new
    appearance = SubFactory('factories.AppearanceFactory')
    outcome = SubFactory('factories.OutcomeFactory')

    class Meta:
        model = Contender


class ConventionFactory(DjangoModelFactory):
    name = Faker('city')
    status = Convention.STATUS.new
    season = Convention.SEASON.summer
    panel = Convention.PANEL.quintiple
    year = 2017
    open_date = datetime.date(2017, 6, 1)
    close_date = datetime.date(2017, 6, 30)
    start_date = datetime.date(2017, 7, 1)
    end_date = datetime.date(2017, 7, 8)
    location = "Nashville, TN"
    timezone = 'US/Central'
    venue = None
    group = SubFactory('factories.GroupFactory')

    class Meta:
        model = Convention

    # @post_generation
    # def create_assignments(self, create, extracted, **kwargs):
    #     if create:
    #         AssignmentFactory(
    #             convention=self,
    #             category=Assignment.CATEGORY.drcj,
    #         )
    #         AssignmentFactory(
    #             convention=self,
    #             category=Assignment.CATEGORY.ca,
    #         )
    #         for i in range(self.panel):
    #             AssignmentFactory(
    #                 convention=self,
    #                 category=Assignment.CATEGORY.music,
    #             )
    #             AssignmentFactory(
    #                 convention=self,
    #                 category=Assignment.CATEGORY.performance,
    #             )
    #             AssignmentFactory(
    #                 convention=self,
    #                 category=Assignment.CATEGORY.singing,
    #             )


class EntryFactory(DjangoModelFactory):
    status = Entry.STATUS.new
    is_evaluation = True
    is_private = False
    session = SubFactory('factories.SessionFactory')
    group = SubFactory('factories.GroupFactory')

    class Meta:
        model = Entry


class GroupFactory(DjangoModelFactory):
    name = Faker('company')
    status = Group.STATUS.active
    kind = Group.KIND.quartet
    code = ''
    start_date = None
    end_date = None
    email = Faker('email')
    phone = Faker('phone_number')
    location = ''
    website = ''
    facebook = ''
    twitter = ''
    image = ''
    description = ''
    notes = ''
    bhs_id = Sequence(lambda x: x)
    parent = None

    class Meta:
        model = Group

    # @post_generation
    # def create_members(self, create, extracted, **kwargs):
    #     if create:
    #         if self.kind == self.KIND.quartet:
    #             size = 4
    #         else:
    #             size = 20
    #         for i in range(size):
    #             MemberFactory.create(group=self)

    # @post_generation
    # def create_repertories(self, create, extracted, **kwargs):
    #     if create:
    #         for i in range(6):
    #             RepertoryFactory.create(group=self)


class MemberFactory(DjangoModelFactory):
    status = Member.STATUS.active
    part = Iterator([
        Member.PART.tenor,
        Member.PART.lead,
        Member.PART.baritone,
        Member.PART.bass,
    ])
    group = SubFactory('factories.GroupFactory')
    person = SubFactory('factories.PersonFactory')

    class Meta:
        model = Member


class OfficeFactory(DjangoModelFactory):
    name = Faker('word')
    status = Office.STATUS.active
    kind = Office.KIND.international

    class Meta:
        model = Office


class OfficerFactory(DjangoModelFactory):
    status = Officer.STATUS.new
    start_date = None
    end_date = None
    office = SubFactory('factories.OfficeFactory')
    person = SubFactory('factories.PersonFactory')
    group = SubFactory('factories.GroupFactory')

    class Meta:
        model = Officer


class OutcomeFactory(DjangoModelFactory):
    round = SubFactory('factories.RoundFactory')
    award = SubFactory('factories.AwardFactory')

    class Meta:
        model = Outcome


class PanelistFactory(DjangoModelFactory):
    status = Panelist.STATUS.new
    kind = Panelist.KIND.official
    category = Panelist.CATEGORY.drcj
    round = SubFactory('factories.RoundFactory')
    person = SubFactory('factories.PersonFactory')

    class Meta:
        model = Panelist


@mute_signals(pre_delete, post_save)
class PersonFactory(DjangoModelFactory):
    # name = Faker('name_male')
    first_name = Faker('first_name_male')
    middle_name = ''
    last_name = Faker('last_name_male')
    nick_name = ''
    status = Person.STATUS.active
    birth_date = None
    location = ''
    website = ''
    email = None
    image = ''
    description = ''
    notes = ''
    bhs_id = Sequence(lambda x: '1{0:05d}'.format(x))

    class Meta:
        model = Person


class RepertoryFactory(DjangoModelFactory):
    status = Repertory.STATUS.active
    group = SubFactory('factories.GroupFactory')
    chart = SubFactory('factories.ChartFactory')

    class Meta:
        model = Repertory


class RoundFactory(DjangoModelFactory):
    status = Round.STATUS.new
    kind = Round.KIND.finals
    num = 1
    session = SubFactory('factories.SessionFactory')

    class Meta:
        model = Round


class ScoreFactory(DjangoModelFactory):
    status = Score.STATUS.new
    points = FuzzyInteger(50, 90)
    song = SubFactory('factories.SongFactory')
    panelist = SubFactory('factories.PanelistFactory')

    class Meta:
        model = Score


class SessionFactory(DjangoModelFactory):
    status = Session.STATUS.new
    kind = Session.KIND.quartet
    is_invitational = False
    num_rounds = 2
    convention = SubFactory('factories.ConventionFactory')

    class Meta:
        model = Session

    # @post_generation
    # def create_rounds(self, create, extracted, **kwargs):
    #     if create:
    #         for i in range(self.num_rounds):
    #             num = i + 1
    #             kind = self.num_rounds - i
    #             RoundFactory(
    #                 session=self,
    #                 num=num,
    #                 kind=kind,
    #             )


class SongFactory(DjangoModelFactory):
    status = Song.STATUS.new
    num = 1
    appearance = SubFactory('factories.AppearanceFactory')
    chart = None

    class Meta:
        model = Song



class GridFactory(DjangoModelFactory):
    status = Grid.STATUS.new
    round = SubFactory('factories.RoundFactory')

    class Meta:
        model = Grid


class VenueFactory(DjangoModelFactory):
    name = 'Test Convention Center'
    status = Venue.STATUS.active
    city = 'Nashville'
    state = 'TN'
    airport = 'NTA'
    timezone = 'US/Central'

    class Meta:
        model = Venue

@mute_signals(pre_delete, post_save)
class UserFactory(DjangoModelFactory):
    username = Faker('uuid4')
    password = PostGenerationMethodCall('set_password', 'password')
    is_staff = False

    class Meta:
        model = User