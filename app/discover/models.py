from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse

from tinymce.models import HTMLField


class DiscoverCategory(models.Model):
    title = models.CharField(unique=True, max_length=200, verbose_name='Τίτλος')
    title_eng = models.CharField(unique=True, max_length=200, verbose_name='Τίτλος Αγγλικα')

    def __str__(self):
        return self.title


class Discover(models.Model):
    active = models.BooleanField(default=True, verbose_name='Κατάσταση')
    # first_page = models.BooleanField(default=False, verbose_name='Αρχική Σελίδα')
    image = models.ImageField(upload_to='discovers/', null=True, help_text='500*500')
    big_image = models.ImageField(upload_to='big_images/discovers/', null=True, help_text='1200*500')
    is_favorite = models.BooleanField(default=True, verbose_name='Προτεινόμενο')
    category = models.ForeignKey(DiscoverCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(unique=True, max_length=250, verbose_name='Τίτλος')
    text = HTMLField(verbose_name='Περιγραφή')
    title_eng = models.CharField(unique=True, max_length=2000, verbose_name='Τίτλος στα Αγγλικά')
    text_eng = HTMLField(verbose_name='Περιγραφή στα Αγγλικά')
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True, allow_unicode=True, max_length=240, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('discover_detail_view', kwargs={'slug': self.slug})

    def get_absolute_eng_url(self):
        return reverse('discover_detail_eng', kwargs={'slug': self.slug})


@receiver(post_save, sender=Discover)
def update_slug_on_discover(sender, instance,  **kwargs):
    slug = instance.slug
    if not slug:
        new_slug = slugify(instance.title, allow_unicode=True)
        qs_exists = Discover.objects.filter(slug=new_slug).exists()
        instance.slug = f'{new_slug}-{instance.id}' if qs_exists else new_slug
        instance.save()