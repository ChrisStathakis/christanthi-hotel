from django.db import models


class BannerManager(models.Manager):

    def get_active(self):
        return super().filter(active=True)

    def first_banners(self):
        return self.get_active().filter(category='1')

    def right_banners(self):
        return self.get_active().filter(category='b')

    def left_banners(self):
        return self.get_active().filter(category='1')