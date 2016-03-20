from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^signup/', views.sign_up, name='signup'),
    url(r'^id/(?P<sock_id>[0-9]+)/$', views.id, name='sock_by_id'),
    url(r'^material/(?P<material>[A-Za-z]+)/$', views.material, name='sock_by_material'),
    url(r'^color/(?P<color>[A-Za-z]+)/$', views.color, name='sock_by_color'),
    url(r'^theme/(?P<theme>[A-Za-z]+)/$', views.theme, name='sock_by_theme'),
    url(r'^admin/', include(admin.site.urls)),
]
