
from django.contrib import admin
from django.urls import path
from django.views.generic.detail import DetailView
from django.contrib.auth import views as auth_view
from .views import register

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='accounts_login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='accounts_logout'),
    path('register/', register, name='accounts_register')

]
