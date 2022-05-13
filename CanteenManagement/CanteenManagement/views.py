from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to canteen ORTAD")

def home(request):
    return HttpResponse("This is Home Page ")

def login(request):
    return HttpResponse("This is login Page ")


