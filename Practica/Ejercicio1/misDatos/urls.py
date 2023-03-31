from django.urls import path
from misDatos import views

urlpatterns=[
    path('',views.index,name='index')
]
