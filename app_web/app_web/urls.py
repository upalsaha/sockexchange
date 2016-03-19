from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Examples:
    url(r'^home/', views.home, name='home'),
    url(r'^detail/(?P<sock_id>[0-9]+)/$', views.detail, name='detail_sock_by_id'),
]

urlpatterns += staticfiles_urlpatterns()