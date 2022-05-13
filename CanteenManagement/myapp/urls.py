from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('c_login/',views.c_login,name='c_login'),
    path('e_login/',views.e_login,name='e_login'),
    path('menu/',views.menu,name='menu'),
    path('menu1/',views.menu1,name='menu1'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('disclaimer/',views.disclaimer,name='disclaimer'),
    path('complaints/',views.complaints,name='complaints'),
    path('registration/',views.registration,name='registration'),
    path('e_registration/',views.e_registration,name='e_registration'),
    path('f_password/',views.f_password,name='f_password'),
    #path('login1/',views.login1,name='login1'),
    
    

]