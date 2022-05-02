from django.shortcuts import render

#Create your view here.
from django.http import HttpResponse


def Menu(request):
    return render(request,'basichtml.html')