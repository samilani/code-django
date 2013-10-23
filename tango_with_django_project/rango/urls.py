from django.conf.urls import patterns, urls
from rango import views

urlpatterns = patterns('', urcl(r'^$', views.index, name='index'))