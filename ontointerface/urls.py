from django.urls import path

from . import views

app_name = 'ontointerface'

urlpatterns = [
    path('', views.index, name='index'),
    path('access_granted', views.access_granted, name='access_granted'),
    path('access_denied', views.access_denied, name='access_denied')
]

