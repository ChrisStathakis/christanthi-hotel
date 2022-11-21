from django.contrib import admin
from .models import Banner, Instagram, Contact


@admin.register(Instagram)
class InstagramAdmin(admin.ModelAdmin):
    fields = ['url', 'active']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_filter = ['category', ]
    list_display = ['id', 'image', 'category']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'email', 'title', 'name', 'is_readed']
    list_filter = ['is_readed']
    search_fields = ['name', 'email', 'title']
