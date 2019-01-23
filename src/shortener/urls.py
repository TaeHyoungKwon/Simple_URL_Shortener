from django.conf.urls import url

from . import views
from .views import ChartData


urlpatterns = [

    # URL for general view
    url(r'^$', views.shortener_home, name='home'),
    url(r'^list$', views.url_list, name='url_list'),
    url(r'^analysis$', views.analysis, name='analysis'),

    # API request URL
    url(r'^chart/data$', ChartData.as_view(), name='api-data'),

    # Detail Page for Shortened URL
    url(r'^(?P<additional_url>[\w-]+)/status$',
        views.shortener_detail, name='detail'),

    # Redirect URL
    url(r'^(?P<additional_url>[\w-]+)$',
        views.redirect_origin_url, name='redirect'),

]
