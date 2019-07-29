from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

def Home(request):
    return HttpResponse("<h1>你好</h1>")
