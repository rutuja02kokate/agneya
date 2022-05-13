from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render (request,'home.html')


#def login(request):
 #   return render(request,'login.html')

#def c_login(request):        for customer
 #   return render(request,'c_login.html')

# function for employee login
def e_login(request):
    return render(request,'e_login.html')

# function for home page menu 
def menu1(request):
    return render(request,'menu1.html')

# function for menu after customer login
def menu(request):
    return render(request,'menu.html')

# function for about page of canteen
def about(request):
    return render(request,'about.html')

# function for contact details 
def contact(request):
    return render(request,'contact.html')

# function for disclimer page 
def disclaimer(request):
    return render(request,'disclaimer.html')

# function for complaint 
def complaints(request):
    return render(request,'complaints.html')


#function for customer login
def registration(request):   
    return render(request,'registration.html')

#function for employee registration
def e_registration(request):
    return render(request,'e_registration.html')

#function for forgot password
def f_password(request):
    return render(request,'f_password.html')

#function for customer login 
def c_login(request):
    return render(request,'c_login.html') 