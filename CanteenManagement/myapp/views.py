from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render (request,'home.html')


def login(request):
    return render(request,'login.html')

def menu(request):
    return render(request,'menu.html')

def about(request):
    return render(request,'about.html')

def registration(request):
    return render(request,'registration.html')

