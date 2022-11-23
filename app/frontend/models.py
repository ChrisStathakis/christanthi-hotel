from django.db import models
from django.core.mail import send_mail
from tinymce.models import HTMLField
from django.conf import settings

from .managers import BannerManager
# Create your models here.

SITE_EMAIL = settings.SITE_EMAIL


class Instagram(models.Model):
    active = models.BooleanField(default=True)
    url = models.TextField(null=True)

    def __str__(self):
        return f'Instagram Photo {self.id}'


class Banner(models.Model):
    SIZE_TYPE = (
        ('1', 'ΒΑΣΙΚΟ ΑΡΙΣΤΕΡΑ => (845*815)'),
        ('b', 'ΒΑΣΙΚΟ ΔΕΞΙΑ => (845*815)'),
        ('2', 'Second Banner'),
        ('3', 'About Page')
    )
    active = models.BooleanField(default=True, verbose_name='ΚΑΤΑΣΤΑΣΗ')
    category = models.CharField(default='1', max_length=1, choices=SIZE_TYPE, verbose_name='ΚΑΤΗΓΟΡΙΑ')
    image = models.ImageField(upload_to='banners/', verbose_name='ΕΙΚΟΝΑ')
    title = models.CharField(max_length=240, null=True, blank=True)
    objects = models.Manager()
    my_query = BannerManager()

    def __str__(self):
        return f'Image {self.id}'


class Contact(models.Model):
    CATEGORY_TYPES = (
        ('a', 'Γενική Ερώτηση - General question'),
        ('b', 'Κρατήσεις - Booking Info'),
    )
    email = models.EmailField()
    category = models.CharField(max_length=1, choices=CATEGORY_TYPES, null=True, verbose_name='Κατηγορία')
    title = models.CharField(max_length=200, verbose_name='Θέμα')
    name = models.CharField(max_length=200, verbose_name='Ονοματεπώνυμο', null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, verbose_name='Τηλέφωνο')
    text = HTMLField(verbose_name='Μήνυμα')
    is_readed = models.BooleanField(default=False, verbose_name='ΔΙΑΒΑΣΜΕΝΟ')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['is_readed', ]

    def __str__(self):
        return self.title

    @staticmethod
    def send_email(form, gr=True):
        message = form.cleaned_data.get('title', None)
        email = form.cleaned_data.get('email', None)
        title = 'Σας ευχαριστούμε για την ερώτηση, θα σας απαντήσουμε το συντομότερο δυνατόν' if gr\
            else 'Thank you for the question, we will inform you shortly'
        send_mail(
            title,
            message,
            SITE_EMAIL,
            [email, ],
            fail_silently=True
        )

    @staticmethod
    def inform_admin_email(form):
        title = f'{form.cleaned_data.get("title", " No Title")} | {form.cleaned_data.get("category", "No Category")}'
        message = form.cleaned_data.get('text', None)
        email = form.cleaned_data.get('email', None)
        send_mail(
            title,
            f'{email} | {message}',
            SITE_EMAIL,
            [SITE_EMAIL, ],
            fail_silently=True

        )