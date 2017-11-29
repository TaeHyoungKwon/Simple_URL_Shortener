from django.db import models

class ShortenURL(models.Model):
    origin_url = models.CharField(max_length=200)
    additional_url = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
