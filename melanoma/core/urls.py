from django.contrib import admin
from django.urls import path
from . import views
from core.views import Inicio
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('home/', views.home, name="home"),

]
