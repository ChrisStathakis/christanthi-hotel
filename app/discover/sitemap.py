from django.contrib.sitemaps import Sitemap
from .models import DiscoverCategory


class DiscoverCategorySitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return DiscoverCategory.objects.all()