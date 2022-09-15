from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'greetings/home.html')

def about(request, name):
    return HttpResponse('Coś o stronie...')

def contact(request, name):
    return HttpResponse('Napisz do nas!')