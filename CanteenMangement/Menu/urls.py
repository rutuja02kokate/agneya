from django.contrib import admin
from django.urls import path
from Menu import views
from .views import Menu

urlpatterns = [
    path('', Menu),
]