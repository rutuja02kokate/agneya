from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('menu/',views.menu,name='menu'),
    path('about/',views.about,name='about'),
    path('registration/',views.registration,name='registration'),
    
    

]