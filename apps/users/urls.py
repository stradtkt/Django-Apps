from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^profile/(?P<id>\d+)$', views.profile),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]