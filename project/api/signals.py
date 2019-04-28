import django_rq

# Django
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django_fsm.signals import post_transition
# Local
from .models import Appearance
from .models import Panelist
from .models import Person
from .models import User
from .models import Round

from .tasks import person_post_save_handler
from .tasks import user_post_delete_handler
from .tasks import save_reports_from_round
from .tasks import save_psa_from_panelist
from .tasks import save_csa_from_appearance


# @receiver(post_save, sender=Person)
def person_post_save(sender, instance, created, **kwargs):
    queue = django_rq.get_queue('low')
    queue.enqueue(
        person_post_save_handler,
        instance,
    )
    return


# @receiver(post_delete, sender=User)
def user_post_delete(sender, instance, **kwargs):
    queue = django_rq.get_queue('low')
    queue.enqueue(
        user_post_delete_handler,
        instance,
    )
    return


@receiver(post_transition, sender=Appearance)
def appearance_post_transition(sender, instance, name, source, target, **kwargs):
    if name == 'complete':
        save_csa_from_appearance.delay(instance)
        return
    return

@receiver(post_transition, sender=Panelist)
def panelist_post_transition(sender, instance, name, source, target, **kwargs):
    if name == 'release':
        save_psa_from_panelist.delay(instance)
        return
    return

@receiver(post_transition, sender=Round)
def round_post_transition(sender, instance, name, source, target, **kwargs):
    if name == 'verify':
        save_reports_from_round.delay(instance)
        return
    return