from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    return render(request,'c_registration.html')

def menu(request):
    return render(request,'menu.html')

def index(request):
    return HttpResponse("hii")