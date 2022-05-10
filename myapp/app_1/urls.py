from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('menu', views.menu, name='menu'),
    path('f_password', views.f_password, name='f_password'),
   

]