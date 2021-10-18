from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models


# Create your views here.
from blog.models import Comments


def register_view(request):
    if request.method == "POST":
        data = request.POST
        first_name = data["first_name"]
        last_name = data["last_name"]
        username = data["username"]
        email = data["email"]
        password1 = data["password1"]
        password2 = data["password2"]
        if password1 != password2:
            return render(request, "signup.html")
        if not username:
            return render(request, "signup.html")

        user = User.objects.create_user, models.ForeignKey(Comments,
             username=username, first_name=first_name, last_name=last_name, email=email, password=password1
        )
        return HttpResponse("Ты зарегался")
    return render(request, 'signup.html')


def login_views(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            login(request, user)
            return redirect(f"/blog/")
        else:
            return render(request, 'login.html')
    if request.method == "GET":
        return render(request, "login.html")


def logout_views(request):
    logout(request)
    return HttpResponse('Good by!')


