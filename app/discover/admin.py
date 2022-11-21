from django.contrib import admin
from .models import Discover, DiscoverCategory


@admin.register(DiscoverCategory)
class DiscoverCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_eng']


@admin.register(Discover)
class DiscoverAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_favorite', 'active']
    list_filter = ['active', 'category', 'is_favorite', ]
