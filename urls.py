from django.conf.urls import url
import django.contrib.auth.views
from . import views





urlpatterns = [

    url(r'^$', views.lista, name='lista'),
    #url(r'^m/(?P<pid>\d+)$', views.pokazMenu, name='pokazMenu'),
    #url(r'^a/(?P<pid>\d+)$', views.pokazArtykul, name='pokazArtykul'),
    #url(r'tpayPotwierdzenie$', views.tpayPotwierdzenie , name='tpayPotwierdzenie'),
    #url(r'tpayPotwierdzenie/$', views.tpayPotwierdzenie , name='tpayPotwierdzenie'),
    #url(r'testtpay$', views.testtpay , name='testtpay'),
    #url(r'skladki$', views.skladki , name='skladki'),
    #url(r'zaplac$', views.zaplac , name='zaplac'),
    #url(r'przetwarzajBazaCr$', views.przetwarzajBazaCr , name='przetwarzajBazaCr'),
    #url(r'mtsz/(.+)$', views.pliki , name='pliki'),
    #url(r'(.+)$', views.brakStrony , name='brakStrony'),
]


