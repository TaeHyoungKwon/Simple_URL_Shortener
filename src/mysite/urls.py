from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import redirect

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include("shortener.urls",namespace="shortener")),
    url(r'^$' , lambda r: redirect('shortener:home')),
]
