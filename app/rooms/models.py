from django.db import models
from django.shortcuts import reverse
from tinymce.models import HTMLField


def upload_photo(instance, filename):
    return f'photos/{instance.room.title}/{filename}'


class Room(models.Model):
    BED_OPTIONS = (
        ('1', '1 ΔΙΠΛΟ ΚΡΕΒΑΤΙ'),
        ('2', 'ΜΟΝΟ ΚΡΕΒΑΤΙ'),
        ('3', '1 ΔΙΠΛΟ ΚΡΕΒΑΤΙ-ΚΑΝΑΠΕΣ ΚΡΕΒΑΤΙ'),
        ('4', '1 ΔΙΠΛΟ ΚΡΕΒΑΤΙ ΚΑΙ 2 ΜΟΝΑ ΚΡΕΒΑΤΙΑ')


    )
    BED_OPTIONS_ENG = (
        ('1', '1 DOUBLE BED'),
        ('2', 'SINGLE BED'),
        ('3', '1 DOUBLE BED -SOFA BED'),
        ('4', '1 DOUBLE DED AND 2 SINGLE BEDS')
    )
    active = models.BooleanField(default=True, verbose_name='ΚΑΤΑΣΤΑΣΗ')
    title = models.CharField(max_length=200, unique=True, verbose_name='ΤΙΤΛΟΣ')
    description = HTMLField(blank=True, verbose_name='ΠΕΡΙΓΡΑΦΗ')
    room_size = models.IntegerField(blank=True, verbose_name='ΜΕΓΕΘΟΣ ΔΩΜΑΤΙΟΥ')
    bed_size = models.CharField(default='1', max_length=1, choices=BED_OPTIONS, verbose_name='ΠΕΡΙΓΡΑΦΗ ΚΡΕΒΑΤΙΩΝ')
    maximum_people = models.IntegerField(default=1, verbose_name='ΜΕΓΙΣΤΗ ΧΩΡΗΤΙΚΟΤΗΤΑ')
    maximum_little_people = models.IntegerField(default=0, verbose_name='ΠΑΙΔΙΑ')

    # english fields
    title_eng = models.CharField(unique=True, max_length=200, verbose_name='ΤΙΤΛΟΣ ENG', null=True)
    description_eng = HTMLField(blank=True, verbose_name='ΠΕΡΙΓΡΑΦΗ ENG')
    bed_size_eng = models.CharField(max_length=1, default='1', choices=BED_OPTIONS_ENG, verbose_name='ΠΕΡΙΓΡΑΦΗ ΚΡΕΒΑΤΙΩΝ ENG')
    webatelier_link = models.URLField(blank=True,)
    slug = models.SlugField(blank=True, null=True, allow_unicode=True, max_length=240, db_index=True)
    location = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ΔΩΜΑΤΙΑ'
        verbose_name = 'ΔΩΜΑΤΙΟ'

    def __str__(self):
        return self.title

    def image(self):
        qs = self.images.filter(is_primary=True)
        return qs.first().image if qs.exists() else None

    def my_images(self):
        return self.images.filter(is_primary=False)

    def get_absolute_url(self):
        return reverse('room_detail_gr', kwargs={'slug': self.slug})

    def get_absolute_url_eng(self):
        return reverse('room_detail_eng', kwargs={'slug': self.slug})


class Characteristic(models.Model):
    title = models.CharField(max_length=220, verbose_name='ΤΙΤΛΟΣ', null=True)
    title_eng = models.CharField(max_length=220, verbose_name='ΤΙΤΛΟΣ', null=True)
    rooms = models.ManyToManyField(Room, null=True, verbose_name='ΔΩΜΑΤΙΟ', related_name='chars')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'ΧΑΡΑΚΤΗΡΙΣΤΙΚΑ ΠΡΟΪΌΝΤΟΣ'
        verbose_name = 'ΧΑΡΑΚΤΗΡΙΣΤΙΚΟ'


class Photo(models.Model):
    is_primary = models.BooleanField(default=False, verbose_name='ΒΑΣΙΚΗ PHOTO')
    image = models.ImageField(upload_to=upload_photo, verbose_name='PHOTO', help_text='445*445')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.room}- {self.id}'


