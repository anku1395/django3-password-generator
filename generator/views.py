from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html',{'password':'dewfaggft434f'})


def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get("uppercase"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get("numbers"):  
        characters.extend(list('0123456789'))

    if request.GET.get('specialcharacters'):
        characters.extend(list('!@#$%^&*()_-'))

    length = int(request.GET.get('length'))
    thepassword = ""

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})


def about(request):
    return render(request,'generator/about.html')