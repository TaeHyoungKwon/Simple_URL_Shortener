from django.db import models
from .utils import random_generate_additional_url
from .validation import validate_url, validate_first_essential_part
from django.conf import settings

from datetime import datetime

class ShortenURL(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    origin_url = models.CharField(max_length=200, unique=True, validators=[validate_url, validate_first_essential_part])
    additional_url = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.origin_url)
    
    def save(self, *args, **kwargs):
        self.additional_url = random_generate_additional_url(self)
        super(ShortenURL, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('shortener:detail', kwargs={'additional_url': self.additional_url})

    def get_origin_url(self):
        from django.core.urlresolvers import reverse
        return reverse('shortener:redirect', kwargs={'additional_url': self.additional_url})        



class Information(models.Model):
    shorten_url = models.OneToOneField(ShortenURL, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.shorten_url)


class HitUpdatedTime(models.Model):
    information = models.ForeignKey(Information, related_name='updated_time')
    clicked_user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.information) + str(self.updated_at)