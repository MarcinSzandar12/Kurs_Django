from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def homepage(request):
    t = loader.get_template("infos/homepage.html")
    c = {"title":"Strona Domowa"}
    return HttpResponse(t.render(c))

def me(request):
    t = loader.get_template("infos/me.html")
    c = {"title":"O mnie"}
    return HttpResponse(t.render(c))

def contact(request):
    t = loader.get_template("infos/contact.html")
    c = {"title":"Kontact"}
    return HttpResponse(t.render(c))
