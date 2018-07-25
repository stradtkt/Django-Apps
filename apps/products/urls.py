from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_product$', views.add_product_page),
    url(r'^process_product$', views.process_product),
]