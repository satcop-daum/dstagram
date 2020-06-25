
from django.contrib import admin
from django.urls import path
from django.views.generic.detail import DetailView

from .views import photo_list
from .views import PhotoUploadView, PhotoUpdatView, PhotoDeleteView
from .models import Photo

app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('photo/upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('photo/detail/<int:pk>/'
         , DetailView.as_view(model=Photo, template_name='photo/detail.html'), name='photo_detail'),
    path('photo/update/<int:pk>/', PhotoUpdatView.as_view(), name='photo_update'),
    path('photo/delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete')

]
