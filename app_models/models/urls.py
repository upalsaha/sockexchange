from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^id/(?P<sock_id>[0-9]+)/$', views.id, name='sock_by_id'),
    url(r'^material/(?P<material>[A-Za-z]+)/$', views.material, name='sock_by_material'),
    url(r'^color/(?P<color>[A-Za-z]+)/$', views.color, name='sock_by_color'),
    url(r'^theme/(?P<theme>[A-Za-z]+)/$', views.theme, name='sock_by_theme'),

]
