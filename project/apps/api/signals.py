from django.db.models.signals import (
    post_save,
)

from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from django.conf import settings

from .models import (
    Contest,
)

from .factories import (
    add_sessions,
    add_judges,
)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_post_save(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Contest)
def contest_post_save(sender, instance=None, created=False, raw=False, **kwargs):
    if not raw:
        if created:
            add_sessions(instance)
            add_judges(instance)
            instance.save()
            # instance.build()
            # instance.save()
