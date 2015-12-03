from random import (
    randint,
)

from django.utils import timezone

from factory.django import (
    DjangoModelFactory,
)

from .models import (
    Group,
    Person,
    Contestant,
    Certification,
    Tune,
    Panelist,
    Ranking,
)


def add_panelists(panel):
    admin = Certification.objects.filter(
        category=Certification.CATEGORY.admin,
    ).order_by('?').first()
    panelist = contest.panelists.filter(
        category=Panelist.CATEGORY.admin,
        person=None,
    ).first()
    try:
        panelist.person = person
    except AttributeError:
        return "All spots filled"
    panelist.save()
    persons = Person.objects.filter(
        judge=Person.JUDGE.music,
    ).order_by('?')[:contest.panel]
    for person in persons:
        panelist = contest.panelists.filter(
            category=Panelist.CATEGORY.music,
            person=None,
        ).first()
        panelist.person = person
        panelist.save()
    persons = Person.objects.filter(
        judge=Person.JUDGE.singing,
    ).order_by('?')[:contest.panel]
    for person in persons:
        panelist = contest.panelists.filter(
            category=Panelist.CATEGORY.singing,
            person=None,
        ).first()
        panelist.person = person
        panelist.save()
    persons = Person.objects.filter(
        judge=Person.JUDGE.presentation,
    ).order_by('?')[:contest.panel]
    for person in persons:
        panelist = contest.panelists.filter(
            category=Panelist.CATEGORY.presentation,
            person=None,
        ).first()
        panelist.person = person
        panelist.save()
    return "Panelists Impaneled"


def add_contestants(convention, kind=Group.KIND.quartet, number=20):
    groups = Group.objects.filter(
        kind=kind,
        status=Group.STATUS.active,
    ).order_by('?')[:number]
    for group in groups:
        contestant = Contestant.objects.create(
            convention=convention,
            group=group,
            # prelim=randint(700, 900) * .1,
        )
        contestant.qualify()
        contestant.accept()
        contestant.save()
    return "Contestants Added"


def add_rankings(contest, number=10):
    contestants = contest.convention.contestants.order_by('?')[:number]
    for contestant in contestants:
        Ranking.objects.create(
            contest=contest,
            contestant=contestant,
        )
    return "Rankings Added"


def score_performance(performance):
    base = randint(70, 90)
    songs = performance.songs.all()
    for song in songs:
        song.title = Tune.objects.order_by('?').first().name
        scores = song.scores.all()
        for score in scores:
            low, high = base, base + 5
            score.points = randint(low, high)
            score.save()
        song.save()
    performance.save()
    return "Performance Scored"


def schedule_performances(session):
    performances = session.performances.all()
    for performance in performances:
        performance.start_time = timezone.now()
        performance.prep()
        performance.save()
    return "Performances scheduled"


class QuartetFactory(DjangoModelFactory):
    name = "The Buffalo Bills"
    kind = Group.KIND.quartet

    class Meta:
        model = Group
