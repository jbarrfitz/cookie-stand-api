import random

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class CookieStand(models.Model):
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    min_customers_per_hour = models.IntegerField(default=0)
    max_customers_per_hour = models.IntegerField(default=0)
    avg_cookies_per_sale = models.FloatField(default=0)
    hourly_sales = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('cookie_stand_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.pk and not self.hourly_sales:
            min = self.min_customers_per_hour
            max = self.max_customers_per_hour

            cookies_each_hour = [
                int(random.randomint(min, max)*self.avg_cookies_per_sale)
            ]

