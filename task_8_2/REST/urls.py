from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.crypt_list, name='vi'),
   url(r'^(?P<pk>[0-9]+)/$', views.cript_detail),
    url(r'^data/', views.data_list),
 ]