from django.contrib import admin
from .models import ShortenURL, Information, HitUpdatedTime

admin.site.register(ShortenURL)
admin.site.register(Information)

@admin.register(HitUpdatedTime)
class HitUpdatedTimeAdmin(admin.ModelAdmin):
    list_display = ('information', 'updated_at')