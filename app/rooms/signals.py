from .models import Room
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


@receiver(post_save, sender=Room)
def create_slug_signal(sender, instance, **kwargs):
    slug = instance.slug
    if not slug:
        new_slug = slugify(instance.title, allow_unicode=True)
        qs_exists = Room.objects.filter(slug=new_slug).exists()
        instance.slug = f'{new_slug}-{instance.id}' if qs_exists else new_slug
        instance.save()
