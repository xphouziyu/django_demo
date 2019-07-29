from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse, render

def Home(request):
    return HttpResponse("<h1>你好</h1>")

def login(reques):
    return render(reques, "login.html")
