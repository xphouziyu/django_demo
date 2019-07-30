from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse, render, redirect

def Home(request):
    return HttpResponse("<h1>你好</h1>")

def login(reques):
    if reques.method == "POST":
        name = reques.POST.get('user')
        pwd = reques.POST.get('pwd')
        if name == "alex" and pwd == "123":
            return redirect("http://www.baidu.com")
        else:
            return render(reques, "login.html", {"error_msg": "错误"})
    elif reques.method == "GET":
        return render(reques, "login.html")
