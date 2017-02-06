# Standard Libary
import csv
import logging

# Third-Party
from psycopg2.extras import DateRange

# Django
from django.db import IntegrityError
from django.db.models import Q
from django.utils import (
    dateparse,
    encoding,
)

# Local
from .models import (
    Assignment,
    Award,
    Catalog,
    Chapter,
    Contestant,
    Convention,
    Group,
    Member,
    Organization,
    Performer,
    Person,
    Role,
    Session,
    Submission,
)

log = logging.getLogger(__name__)


def import_db_members(path):
    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)
        rows = [row for row in reader]
        for row in rows:
            if int(row[2]) != 2:
                continue
            chapter_id = int(row[0])
            person_id = int(row[1])
            try:
                p = Person.objects.get(
                    bhs_id=person_id,
                )
            except Person.DoesNotExist:
                print 'No Person'
                continue
            try:
                c = Chapter.objects.get(
                    bhs_id=chapter_id,
                )
            except Chapter.DoesNotExist:
                print 'No Chapter {0}'.format(chapter_id)
                continue
            start = dateparse.parse_date(row[3])
            end = dateparse.parse_date(row[4])
            try:
                mem, create = Member.objects.get_or_create(
                    person=p,
                    chapter=c,
                )
            except IntegrityError:
                print "Integrity {0} - {1}".format(c, p)
                continue
            mem.start_date = start
            mem.end_date = end
            mem.save()
    return "Finished"


def import_db_persons(path):
    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(reader)
        rows = [row for row in reader]
        for row in rows:
            bhs_id = int(row[0])
            first_name = row[4].strip()
            nick_name = row[5].strip()
            if nick_name:
                if nick_name != first_name:
                    nick_name = "({0})".format(nick_name)
            else:
                nick_name = None
            middle_name = row[6].strip()
            last_name = row[7].strip()
            suffix_name = row[8].strip()
            prefix_name = row[2].strip()
            name = " ".join(
                map(
                    (lambda x: encoding.smart_text(x)),
                    filter(
                        None, [
                            prefix_name,
                            first_name,
                            middle_name,
                            last_name,
                            suffix_name,
                            nick_name,
                        ]
                    )
                )
            )
            email = row[9].strip()
            kind = int(row[62])
            bhs_status = int(row[34])
            spouse = row[38].strip()
            try:
                mon = int(row[78])
            except ValueError:
                mon = None
            address1 = row[13].strip()
            address2 = row[14].strip()
            city = row[16].strip()
            state = row[17].strip()
            postal_code = row[18].strip()
            country = row[19].strip()
            if country == 'United States':
                phone = "+1{0}{1}".format(
                    str(row[22]),
                    str(row[23]),
                )
            else:
                phone = None
            start_date = dateparse.parse_date(row[58])
            birth_date = dateparse.parse_date(row[31])
            dues_thru = dateparse.parse_date(row[36])
            defaults = {
                'name': name,
                'email': email,
                'kind': kind,
                'status': bhs_status,
                'spouse': spouse,
                'mon': mon,
                'address1': address1,
                'address2': address2,
                'city': city,
                'state': state,
                'postal_code': postal_code,
                'country': country,
                'phone': phone,
                'start_date': start_date,
                'birth_date': birth_date,
                'dues_thru': dues_thru,
            }
            person, created = Person.objects.update_or_create(
                bhs_id=bhs_id,
                defaults=defaults,
            )
            print person, created


def import_db_quartets(path):
    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(reader)
        rows = [row for row in reader]
        for row in rows:
            if int(row[4]) == 3:
                name = row[2].strip()
                if name.endswith(', The'):
                    name = "The " + name.partition(', The')[0]
                try:
                    created = False
                    g = Group.objects.get(
                        bhs_id=int(row[0]),
                    )
                except Group.DoesNotExist:
                    bhs_id = int(row[0])
                    try:
                        g, created = Group.objects.get_or_create(
                            bhs_id=bhs_id,
                            name=encoding.smart_text(name),
                        )
                    except UnicodeDecodeError:
                        continue
            else:
                continue
            print g, created


def import_db_chapters(path):
    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(reader)
        rows = [row for row in reader]
        for row in rows:
            if int(row[4]) == 4:
                code = row[1].strip()
                name = row[2].partition(" ")[2].strip()
                try:
                    created = False
                    c = Chapter.objects.get(
                        bhs_id=int(row[0]),
                    )
                except Chapter.DoesNotExist:
                    bhs_id = int(row[0])
                    try:
                        c, created = Chapter.objects.get_or_create(
                            bhs_id=bhs_id,
                            code=code,
                            name=encoding.smart_text(name),
                        )
                    except UnicodeDecodeError:
                        continue
                    except IntegrityError:
                        exist = Chapter.objects.get(
                            code=code,
                        )
                        exist.bhs_id = bhs_id
                        exist.save()
                        created = 'UPDATED'
            else:
                continue
            print c, created


def import_db_roles(path):
    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(reader)
        rows = [row for row in reader]
        for row in rows:
            if int(row[12]) not in [1, 2, 3, 4]:
                continue
            try:
                group = Group.objects.get(
                    bhs_id=int(row[1])
                )
            except Group.DoesNotExist:
                log.error("Missing Group {0}: {1}".format(row[1], row[2]))
                continue
            if group.KIND == Group.KIND.chorus:
                log.error("Chorus, not Quartet {0}: {1}".format(row[1], row[2]))
                continue
            try:
                person = Person.objects.get(
                    bhs_id=int(row[3])
                )
            except Person.DoesNotExist:
                person = Person.objects.create(
                    name=encoding.smart_text(row[4]),
                    bhs_id=int(row[3]),
                )
            if int(row[12]) == 1:
                part = Role.PART.tenor
            elif int(row[12]) == 2:
                part = Role.PART.lead
            elif int(row[12]) == 3:
                part = Role.PART.baritone
            elif int(row[12]) == 4:
                part = Role.PART.bass
            else:
                log.error("No Part: {0}".format(row[12]))
                continue
            lower = dateparse.parse_date(row[7])
            if not row[8]:
                upper = None
            else:
                upper = dateparse.parse_date(row[8])
            date = DateRange(
                lower=lower,
                upper=upper,
                bounds="[)",
            )
            if upper and lower:
                if lower > upper:
                    date = None
            role = {
                'bhs_id': int(row[0]),
                'group': group,
                'person': person,
                'date': date,
                'part': part,
            }
            try:
                role, created = Role.objects.get_or_create(
                    **role
                )
            except Role.MultipleObjectsReturned:
                log.error("Multi Roles: {1}".format(group))
                continue
            print role


def import_db_directors(path):
    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(reader)
        rows = [row for row in reader]
        for row in rows:
            if int(row[5]) != 38:
                continue
            else:
                part = Role.PART.director
            groups = Group.objects.filter(
                chapter__bhs_id=int(row[1]),
                status=Group.STATUS.active,
                kind=Group.KIND.chorus,
            )
            if groups.count() > 1:
                log.error("Too many groups {0}: {1}".format(row[1], row[2]))
                continue
            elif groups.count() == 0:
                group = Group.objects.filter(
                    chapter__bhs_id=int(row[1])
                ).first()
                if not group:
                    try:
                        chapter = Chapter.objects.get(bhs_id=int(row[1]))
                    except Chapter.DoesNotExist:
                        log.error("No chapter {0}: {1}".format(row[1], row[2]))
                        continue
                    group, c = Group.objects.get_or_create(
                        chapter=chapter,
                        status=Group.STATUS.inactive,
                        name=row[2].strip(),
                        kind=Group.KIND.chorus,
                    )
            else:
                group = groups.first()
            if group.kind != Group.KIND.chorus:
                log.error("Not a chorus {0}: {1}".format(row[1], row[2]))
                continue
            try:
                person = Person.objects.get(
                    bhs_id=(row[3])
                )
            except Person.DoesNotExist:
                log.error("Missing Person {0}: {1} for {2} {3}".format(
                    row[3],
                    row[4],
                    row[1],
                    row[2],
                ))
                continue
            lower = dateparse.parse_date(row[7])
            if not row[8]:
                upper = None
            else:
                upper = dateparse.parse_date(row[8])
            if lower < upper:
                date = DateRange(
                    lower=lower,
                    upper=upper,
                    bounds="[)",
                )
            else:
                log.error("Date out of sequence: {0} {1}".format(
                    row[7],
                    row[8],
                ))
                date = None
            role = {
                'bhs_id': int(row[0]),
                'group': group,
                'person': person,
                'date': date,
                'part': part,
            }
            try:
                role, created = Role.objects.get_or_create(
                    **role
                )
            except Role.MultipleObjectsReturned:
                log.error("ERROR: Multi Roles: {1}".format(role))
                continue
            print role
        return


def import_db_performers(path):
    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(reader)
        rows = [row for row in reader]
        for row in rows:
            convention_bhs_id = int(row[3])
            group_bhs_id = int(row[2])
            soa = int(row[6]) if int(row[6]) else None
            try:
                convention = Convention.objects.get(
                    bhs_id=convention_bhs_id,
                )
            except Convention.DoesNotExist:
                log.error("No Convention: {0}".format(row[3]))
                continue
            try:
                group = Group.objects.get(
                    bhs_id=group_bhs_id,
                )
            except Group.DoesNotExist:
                try:
                    chapter = Chapter.objects.get(code=row[1][:4])
                    groups = chapter.groups.filter(status=Group.STATUS.active)
                    if groups.count() == 1:
                        group = groups.first()
                        group.bhs_id = group_bhs_id
                        group.save()
                    else:
                        log.error("No Group: {0}, {1}".format(row[2], row[1]))
                        continue
                except Chapter.DoesNotExist:
                    log.error("No Group: {0}, {1}".format(row[2], row[1]))
            if row[7].strip() == 'Normal Evaluation and Coaching':
                is_evaluation = True
            else:
                is_evaluation = False
            try:
                session = convention.sessions.get(
                    kind=group.kind,
                )
            except Session.DoesNotExist:
                try:
                    session = convention.sessions.get(
                        kind=Session.KIND.youth,
                    )
                except Session.DoesNotExist:
                    log.error("No Session: {0}, {1} - {2}".format(convention, group, group.get_kind_display()))
                    continue
            performer, created = Performer.objects.get_or_create(
                session=session,
                group=group,
            )
            performer.soa = soa
            performer.is_evaluation = is_evaluation
            performer.bhs_id = int(row[0])
            performer.save()


def import_db_submissions(path):
    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)
        rows = [row for row in reader]
        for row in rows:
            bhs_id = int(row[0])
            title = row[1].strip()
            if row[2]:
                bhs_marketplace = int(row[2])
            else:
                bhs_marketplace = None
            if bhs_marketplace:
                try:
                    catalog = Catalog.objects.get(
                        bhs_marketplace=bhs_marketplace,
                    )
                    log.info('Found catalog by marketplace')
                except Catalog.DoesNotExist:
                    log.info('No marketplace: {0} {1}'.format(bhs_id, title))
                    catalog = None
            else:
                catalog = None
            if not catalog:
                try:
                    catalog = Catalog.objects.get(
                        title=title,
                        bhs_marketplace=None,
                    )
                    log.info('Found catalog by title')
                except Catalog.DoesNotExist:
                    if bhs_marketplace:
                        catalog = Catalog.objects.create(
                            title=title,
                            bhs_marketplace=bhs_marketplace,
                        )
                        log.info("Create catalog with id: {0} {1}".format(title, bhs_marketplace))
                    else:
                        catalog = Catalog.objects.create(
                            title=title,
                        )
                        log.info("Create catalog with no id: {0}".format(title))
                except Catalog.MultipleObjectsReturned:
                    catalog = Catalog.objects.filter(
                        title=title,
                        bhs_marketplace=None,
                    ).first()
                    log.info("Pick first catalog: {0}".format(title))
            performers = Performer.objects.filter(
                group__bhs_id=bhs_id,
                session__convention__year=2016,
            )
            for performer in performers:
                submission, created = Submission.objects.get_or_create(
                    performer=performer,
                    catalog=catalog,
                )
                print submission, created


def import_db_representing(path):
    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(reader)
        rows = [row for row in reader]
        for row in rows:
            name = row[11].strip()
            if name == 'Div I':
                name = 'Division I Division'
            elif name == 'Div II':
                name = 'Division II Division'
            elif name == 'Div III':
                name = 'Division III Division'
            elif name == 'Div IV':
                name = 'Division IV Division'
            elif name == 'Div V':
                name = 'Division V Division'
            elif name == 'Arizona  Division':
                name = 'Arizona Division'
            elif name == 'Division One':
                name = 'Division One Division'
            elif name == 'Granite & Pine Division':
                name = 'Granite and Pine Division'
            if name != 'NULL':
                convention = Convention.objects.get(
                    bhs_id=int(row[3]),
                )
                district_name = convention.organization.short_name
                try:
                    organization = Organization.objects.get(
                        name="{0} {1}".format(
                            district_name,
                            name,
                        )
                    )
                except Organization.DoesNotExist:
                    log.error("Bad Div: {0} {1}".format(district_name, name))
                    continue
                try:
                    performer = Performer.objects.get(
                        bhs_id=int(row[0]),
                    )
                except Performer.DoesNotExist:
                    log.error("Can't find performer")
                    continue
                performer.representing = organization
                performer.save()


def import_db_contests(path):
    with open(path) as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(reader)
        rows = [row for row in reader]
        for row in rows:
            convention_bhs_id = int(row[3])
            performer_bhs_id = int(row[0])
            try:
                convention = Convention.objects.get(
                    bhs_id=convention_bhs_id,
                )
            except Convention.DoesNotExist:
                log.error("No Convention: {0}".format(row[3]))
                continue
            name = row[8].strip()
            try:
                performer = Performer.objects.get(
                    bhs_id=performer_bhs_id,
                )
            except Performer.DoesNotExist:
                log.error("Can't find performer")
                continue
            try:
                session = convention.sessions.get(
                    kind=performer.group.kind,
                )
            except Session.DoesNotExist:
                try:
                    session = convention.sessions.get(
                        kind=Session.KIND.youth,
                    )
                except Session.DoesNotExist:
                    try:
                        session = convention.sessions.get(
                            kind=Session.KIND.seniors,
                        )
                    except Session.DoesNotExist:
                        log.error("No Session: {0}, {1} - {2}".format(
                            convention,
                            performer.group,
                            performer.group.get_kind_display(),
                        ))
                        continue
            if not performer.representing:
                log.error("No representation for {0}".format(performer))
                continue
            organization = performer.representing
            if organization.level == Organization.LEVEL.district:
                district = organization
                division = None
            elif organization.level == Organization.LEVEL.division:
                district = organization.parent
                division = organization
            else:
                log.error("Bad Rep: {0} {1}".format(
                    performer,
                    organization,
                ))
                continue
            excludes = [
                "International Srs Qt - Oldest Singer",
            ]
            if any([string in name for string in excludes]):
                continue
            if name == 'Scores for Evaluation Only':
                performer.status = Performer.STATUS.evaluation
                performer.save()
                continue
            name = name.replace("Most Improved", "Most-Improved")
            try:
                award = Award.objects.get(
                    organization=performer.representing,
                    stix_name__endswith=name,
                )
            except Award.DoesNotExist:
                if 'International Preliminary Quartet' in name:
                    award = Award.objects.get(
                        name='International Quartet',
                    )
                elif 'International Preliminary Youth Qt' in name:
                    award = Award.objects.get(
                        is_primary=True,
                        level=Award.LEVEL.international,
                        kind=Award.KIND.youth,
                    )
                elif 'International Preliminary Seniors Qt' in name:
                    award = Award.objects.get(
                        is_primary=True,
                        level=Award.LEVEL.international,
                        kind=Award.KIND.seniors,
                    )
                elif 'Quartet District Qualification' in name:
                    award = Award.objects.get(
                        is_primary=True,
                        level=Award.LEVEL.district,
                        kind=Award.KIND.quartet,
                        organization=district,
                    )
                elif 'International Seniors Quartet' in name:
                    award = Award.objects.get(
                        is_primary=True,
                        level=Award.LEVEL.international,
                        kind=Award.KIND.seniors,
                    )
                elif 'International Srs Qt - Oldest Qt' in name:
                    award = Award.objects.get(
                        name='International Oldest Seniors'
                    )
                elif 'Seniors Qt District Qualification (Overall)' in name:
                    award = Award.objects.get(
                        is_primary=True,
                        level=Award.LEVEL.district,
                        kind=Award.KIND.seniors,
                        organization=district,
                    )
                elif 'District Super Seniors Quartet' in name:
                    award = Award.objects.get(
                        name='Far Western District Super Seniors'
                    )
                elif 'Out Of District Qt Prelims (2 Rounds)' in name:
                    award = Award.objects.get(
                        name='International Quartet',
                    )
                elif 'Out of Division Quartet (Score)' in name:
                    award = Award.objects.get(
                        is_primary=True,
                        level=Award.LEVEL.district,
                        kind=Award.KIND.quartet,
                        organization=district,
                    )
                elif 'Out Of Division Seniors Quartet' in name:
                    award = Award.objects.get(
                        is_primary=True,
                        level=Award.LEVEL.district,
                        kind=Award.KIND.seniors,
                        organization=district,
                    )
                elif 'Out Of Division Quartet (Overall)' in name:
                    award = Award.objects.get(
                        is_primary=True,
                        level=Award.LEVEL.district,
                        kind=Award.KIND.quartet,
                        organization=district,
                    )
                elif 'International Chorus' == name:
                    award = Award.objects.get(
                        name='International Chorus',
                    )
                elif 'International Preliminary Chorus' == name:
                    award = Award.objects.get(
                        name='International Chorus',
                    )
                elif 'Chorus District Qualification' in name:
                    award = Award.objects.get(
                        is_primary=True,
                        level=Award.LEVEL.district,
                        kind=Award.KIND.chorus,
                        organization=district,
                    )
                elif 'Most-Improved Chorus' in name:
                    award = Award.objects.get(
                        level=Award.LEVEL.district,
                        kind=Award.KIND.chorus,
                        organization=district,
                        is_improved=True,
                    )
                elif 'Out Of Division Chorus' in name:
                    award = Award.objects.get(
                        is_primary=True,
                        level=Award.LEVEL.district,
                        kind=Award.KIND.chorus,
                        organization=district,
                    )
                elif 'Plateau A (or 1) Chorus' == name:
                    if row[4] == 'Division Only':
                        organization = division
                        level = Award.LEVEL.division
                    else:
                        organization = district
                        level = Award.LEVEL.district
                    if "Improved" in name:
                        is_improved = True
                    else:
                        is_improved = False
                    award = Award.objects.get(
                        Q(
                            stix_name__contains='Plateau A ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ) | Q(
                            stix_name__contains='Plateau 1 ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ) | Q(
                            stix_name__contains='Plateau I ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ),
                    )
                elif 'Plateau AA (or 2) Chorus' == name:
                    if row[4] == 'Division Only':
                        organization = division
                        level = Award.LEVEL.division
                    else:
                        organization = district
                        level = Award.LEVEL.district
                    if "Improved" in name:
                        is_improved = True
                    else:
                        is_improved = False
                    award = Award.objects.get(
                        Q(
                            stix_name__contains='Plateau AA ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ) | Q(
                            stix_name__contains='Plateau 2 ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ) | Q(
                            stix_name__contains='Plateau II ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ),
                    )
                elif 'Plateau AAA (or 3) Chorus' == name:
                    if row[4] == 'Division Only':
                        organization = division
                        level = Award.LEVEL.division
                    else:
                        organization = district
                        level = Award.LEVEL.district
                    if "Improved" in name:
                        is_improved = True
                    else:
                        is_improved = False
                    award = Award.objects.get(
                        Q(
                            stix_name__contains='Plateau AAA ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ) | Q(
                            stix_name__contains='Plateau 3 ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ) | Q(
                            stix_name__contains='Plateau III ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ),
                    )
                elif 'Plateau AAAA (or 4) Chorus' == name:
                    if row[4] == 'Division Only':
                        organization = division
                        level = Award.LEVEL.division
                    else:
                        organization = district
                        level = Award.LEVEL.district
                    if "Improved" in name:
                        is_improved = True
                    else:
                        is_improved = False
                    award = Award.objects.get(
                        Q(
                            stix_name__contains='Plateau AAAA ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ) | Q(
                            stix_name__contains='Plateau 4 ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ) | Q(
                            stix_name__contains='Plateau IV ',
                            level=level,
                            kind=Award.KIND.chorus,
                            organization=organization,
                            is_improved=is_improved,
                        ),
                    )
                elif 'Division Quartet' == name:
                    if not division:
                        log.error("Div with no Div: {0}".format(performer))
                        continue
                    award = Award.objects.get(
                        is_primary=True,
                        level=Award.LEVEL.division,
                        kind=Award.KIND.quartet,
                        organization=division,
                    )
                else:
                    log.error(
                        "No Award: {0}, {1} {2}".format(
                            name,
                            district,
                            division,
                        )
                    )
                    continue
            except Award.MultipleObjectsReturned:
                log.error("Multiawards")
                continue
            contest, foo = session.contests.get_or_create(
                award=award,
            )
            contestant, created = Contestant.objects.get_or_create(
                contest=contest,
                performer=performer,
            )
            print contestant, created


def update_panel_size(convention):
    for session in convention.sessions.all():
        session.size = session.assignments.filter(
            kind=Assignment.KIND.official,
            category=Assignment.CATEGORY.music,
        ).count()
        session.save()
    return


def denormalize(convention):
    for session in convention.sessions.all():
        for performer in session.performers.all():
            for performance in performer.performances.all():
                for song in performance.songs.all():
                    song.calculate()
                    song.save()
                performance.calculate()
                performance.save()
            performer.calculate()
            performer.save()
        for contest in session.contests.all():
            contest.rank()
            contest.save()
    return


def rank(convention):
    for session in convention.sessions.all():
        session.rank()
        session.save()
        for contest in session.contests.all():
            contest.rank()
            contest.save()
        for round in session.rounds.all():
            round.rank()
            round.save()
    return


def calculate(convention):
    for session in convention.sessions.all():
        for performer in session.performers.all():
            for performance in performer.performances.all():
                for song in performance.songs.all():
                    song.calculate()
                    song.save()
                performance.calculate()
                performance.save()
            performer.calculate()
            performer.save()
            for contestant in performer.contestants.all():
                contestant.calculate()
                contestant.save()
    return


def chapter_district(chapter):
    if not chapter.code:
        log.error("No Chapter Code for {0}".format(chapter))
        return
    else:
        letter = chapter.code[:1]
        chapter.organization = Organization.objects.get(code=letter)


def generate_cycle(year):
    conventions = Convention.objects.filter(
        year=year - 1,
    )
    log.info(conventions)
    for convention in conventions:
        new_v, f = Convention.objects.get_or_create(
            season=convention.season,
            division=convention.division,
            year=convention.year + 1,
            organization=convention.organization
        )
        log.info("{0}, {1}".format(new_v, f))
        sessions = convention.sessions.all()
        for session in sessions:
            new_s, f = new_v.sessions.get_or_create(
                kind=session.kind,
            )
            log.info("{0}, {1}".format(new_s, f))
            rounds = session.rounds.all()
            for round in rounds:
                new_r, f = new_s.rounds.get_or_create(
                    kind=round.kind,
                    num=round.num,
                )
                log.info("{0}, {1}".format(new_r, f))
            assignments = session.assignments.filter(kind=Assignment.KIND.official)
            for assignment in assignments:
                new_j, f = new_s.assignments.get_or_create(
                    category=assignment.category,
                    kind=assignment.kind,
                    slot=assignment.slot,
                )
                log.info("{0}, {1}".format(new_j, f))
            contests = session.contests.all()
            for contest in contests:
                new_c, f = new_s.contests.get_or_create(
                    award=contest.award,
                    session=contest.session,
                    cycle=contest.cycle + 1,
                    is_qualifier=contest.is_qualifier
                )
                log.info("{0}, {1}".format(new_c, f))
    return "Built {0}".format(year)
