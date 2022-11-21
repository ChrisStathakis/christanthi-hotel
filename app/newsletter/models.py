from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse_lazy

from tinymce.models import HTMLField


class NewsLetterPage(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(unique=True, max_length=200, verbose_name='ΤΙΤΛΟΣ ΣΤΑ ΕΛΛΗΝΙΚΑ')
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='news_letter_images')
    text = HTMLField(null=True, verbose_name='ΚΕΙΜΕΝΟ ΣΤΑ ΕΛΛΗΝΙΚΑ')

    title_eng = models.CharField(unique=True, max_length=200, verbose_name='ΤΙΤΛΟΣ ΣΤΑ ΑΓΓΛΙΚΑ')
    text_eng = HTMLField(null=True, verbose_name='ΚΕΙΜΕΝΟ ΣΤΑ ΑΓΓΛΙΚΑ')

    def __str__(self):
        return self.title

    def my_url(self):
        return reverse_lazy('newsletter:newsletter_page_view', kwargs={'slug': self.slug})


class NewsLetter(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    cell_phone = models.CharField(max_length=200, blank=True)
    acceptRules = models.BooleanField(default=False)
    newsletterPage = models.ForeignKey(NewsLetterPage, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.email





@receiver(post_save, sender=NewsLetterPage)
def create_slug_signal(sender, instance, **kwargs):
    slug = instance.slug
    if not slug:
        new_slug = slugify(instance.title, allow_unicode=True)
        qs_exists = NewsLetterPage.objects.filter(slug=new_slug).exists()
        instance.slug = f'{new_slug}-{instance.id}' if qs_exists else new_slug
        instance.save()