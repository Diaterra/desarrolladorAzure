from django.urls import path
from django.http import HttpResponse
from gestion import views

urlpatterns=[
    path('',views.index, name='index'),
    path('futbol', views.equipo, name='equipo'),
    path('madrid', views.jugadores, name='jugadores'),
    path('amigos', views.data, name='amigos'),
    path('peli', views.peli, name='peli'),
]

