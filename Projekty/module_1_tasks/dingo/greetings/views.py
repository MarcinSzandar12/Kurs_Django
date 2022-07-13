from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World!")

def hello_someone(request, name):
    return HttpResponse(f'Hello {str.title(name)}')