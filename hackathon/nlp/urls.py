from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^feedback/send/$', views.secondview, name='secondview'),
    url(r'^feedback/send1/$', views.thirdview, name='thirdview'),
]

