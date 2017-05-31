from django.conf.urls import url, include
from . import views
from rest_framework import routers

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'crypto', views.Crypt_ViewSet, 'crypto')
router.register(r'data', views.Data_ViewSet, 'data')
router.register(r'dataAll', views.Crypto_ViewSetAll, 'dataAll')

urlpatterns = [

    #url(r'^$', views.Crypt_List.as_view(), name='data'),
    #url(r'^(?P<pk>[0-9]+)/$', views.Cript_Detail.as_view()),
    #url(r'^data/$', views.Data_List.as_view()),
    #
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^data/(?P<pk>[0-9]+)/$', views.data_detail, name='data_detail')
 ]