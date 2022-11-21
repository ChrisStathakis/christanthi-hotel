from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewsSitemap(Sitemap):
    priority = 0.5
    changefreq = 'never'

    def items(self):
        return ['homepage_gr', 'room_list_gr', 'discover_list_gr', 'homepage_eng',
                'room_list_eng', 'contact_gr', 'discover_list_eng', 'contact_eng',
                ]

    def location(self, obj):
        return reverse(obj)

