from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Workers
from .helper import slugify


@receiver(pre_save, sender=Workers, dispatch_uid='signal_create_slug')
def signal_create_slug(*args, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify("{} {}".format(
            instance.first_name,
            instance.last_name,
        ))
        instance.save()
    else:
        pass
