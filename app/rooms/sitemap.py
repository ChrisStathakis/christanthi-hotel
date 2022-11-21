from django.contrib.sitemaps import Sitemap

from .models import Room


class RoomSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Room.objects.filter(active=True)