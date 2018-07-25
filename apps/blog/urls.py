from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_blog$', views.add_blog),
    url(r'^process_blog$', views.process_blog),
    url(r'^(?P<id>\d+)/post$', views.post),
    url(r'^(?P<id>\d+)/delete$', views.delete_post),
    url(r'^(?P<id>\d+)/post/process_comment$', views.process_comment),
]