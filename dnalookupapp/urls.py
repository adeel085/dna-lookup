from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('filter', views.filter, name='filter'),
    path('sequence/create', views.sequence, name='sequence'),
    path('sequence/read', views.sequence, name='sequence'),
    path('sequence/update', views.sequence, name='sequence'),
    path('sequence/delete', views.sequence, name='sequence'),
]
