from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def menu(request):
    return render(request,'menu_principal.html')

def about(request):
    return render(request,'about.html')
