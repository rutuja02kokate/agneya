from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request,'c_login.html')

def registration(request):
    return render(request,'c_registration.html')

def menu(request):
    return render(request,'menu.html')

def f_password(request):
    return render(request,'f_password.html')

def index(request):
    return render(request,'home.html')
