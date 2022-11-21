from django.contrib import admin
from .models import Room, CharacteristicsCategory, Characteristic, Photo, CharTitle


class PhotoInline(admin.TabularInline):
    model = Photo


class CharInline(admin.TabularInline):
    model = Characteristic

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'size_in_tm']
    inlines = [PhotoInline, CharInline]

    fieldsets = (
        (None, {
            'fields': ('active',
                       ('room_size', 'maximum_people', 'maximum_little_people'),
                       ('webatelier_link', 'slug')
                       )
        }),
        ('Greek Options',{
            'fields': (('title', 'bed_size'),
                       'description'
                       )
        }),
        ('English Option', {
            'fields': (('title_eng', 'bed_size_eng'),
                       'description_eng'
                       )
        })
    )
    def size_in_tm(self, obj):
        return f'{obj.room_size} τ.μ'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['image', 'room', 'is_primary']


@admin.register(CharacteristicsCategory)
class CharCateAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_eng', 'active']


@admin.register(Characteristic)
class CharAdmin(admin.ModelAdmin):
    pass


@admin.register(CharTitle)
class CharTitleAdmin(admin.ModelAdmin):
    pass