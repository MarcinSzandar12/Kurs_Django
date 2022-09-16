from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request, 'greetings/welcome.html')

def about(request):
    return HttpResponse('Coś o stronie...')

def contact(request):
    return HttpResponse('Napisz do nas!')