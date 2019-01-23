from datetime import datetime

from django.conf import settings
from django.db import models

from .utils import random_generate_additional_url
from .validation import validate_url, validate_first_essential_part


class ShortenURL(models.Model):
    '''
    * Each origin_url will change like "localhost:8000/ADDITIONAL_URL"
    * 'additional_url' is generated by 'random_generate_additional_url' function in utils.py
    '''
    #owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    origin_url = models.CharField(max_length=200, unique=True, validators=[
                                  validate_url, validate_first_essential_part])
    additional_url = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return str(self.origin_url)

    def save(self, *args, **kwargs):
        '''
        * Save additional_url to DB from generated value by random_generate_additional_url
        '''
        self.additional_url = random_generate_additional_url(self)
        super(ShortenURL, self).save(*args, **kwargs)

    def get_absolute_url(self):
        '''
        * Return detail url like "/ADDITIONAL_URL/status"
        '''
        from django.core.urlresolvers import reverse
        return reverse('shortener:detail', kwargs={'additional_url': self.additional_url})

    def get_origin_url(self):
        '''
        * Return redirect url like "/ADDITIONAL_URL/"
        '''
        from django.core.urlresolvers import reverse
        return reverse('shortener:redirect', kwargs={'additional_url': self.additional_url})


class Information(models.Model):
    '''
    * Each Shorten URLs has distinct information that is 'hit
    * 'hit' means count that is clicked shortened link by some users
    '''
    shorten_url = models.OneToOneField(ShortenURL, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.shorten_url)


class HitUpdatedTime(models.Model):
    '''
    * When Shorten URL link is clicked, hit count will add 1 and HitUpdatedTime Log will updated by clicked_user
    '''
    information = models.ForeignKey(Information, related_name='updated_time')
    #clicked_user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.information) + str(self.updated_at)
