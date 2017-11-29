from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.shortener_home,name='home'),
    url(r'^(?P<additional_url>[\w-]+)/$',views.shortener_detail, name='detail'),
]