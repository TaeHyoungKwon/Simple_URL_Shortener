from django.db import models
from .utils import random_generate_additional_url

class ShortenURL(models.Model):
    origin_url = models.CharField(max_length=200, unique=True)
    additional_url = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.origin_url
    
    def save(self, *args, **kwargs):
        self.additional_url = random_generate_additional_url()
        super(ShortenURL, self).save(*args, **kwargs)
