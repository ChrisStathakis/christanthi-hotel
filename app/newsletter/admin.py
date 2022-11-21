from django.contrib import admin

# Register your models here.


from .models import NewsLetter, NewsLetterPage


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['email', 'newsletterPage', 'acceptRules']
    list_filter = ['acceptRules', 'newsletterPage']
    search_fields = ['email', ]
    list_select_related = ['newsletterPage']


@admin.register(NewsLetterPage)
class NewsLetterPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'my_url', 'active']
    list_filter = ['active', ]
    search_fields = ['title', ]
    readonly_fields = ['my_url']
    fields = ['active', 'title', 'image', 'text', 'title_eng', 'text_eng', 'slug']
