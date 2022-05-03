from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def user(request):
    return render(request,'base.html')







