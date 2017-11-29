from django.contrib import admin
from .models import ShortenURL, Information

admin.site.register(ShortenURL)
admin.site.register(Information)
