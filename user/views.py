from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from .models import *


# Profile

def profile(request):

    return render(request, 'profile/profile.html')

# Auth

def log_in(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username = email, password = password)

        if user:

            login(request, user)

            return redirect('app:home')

        else:

            # send json response with incorrect user/password
            pass 

    return render(request, 'auth/login.html')


def register(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(username = email)
        user.set_password(password)
        user.save()

        user.profile.name = name
        user.profile.save()

        user = authenticate(username = email, password = password)
        login(request, user)

        return redirect('app:home')

    return render(request, 'auth/register.html')

