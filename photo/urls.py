
from django.contrib import admin
from django.urls import path

from .views import photo_list

app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),
]
