from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from .models import *

def log_in(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

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

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User(username = username)
        user.set_password(password)
        user.save()

        user.profile.name = name
        user.profile.save()

        user = authenticate(username = username, password = password)
        login(request, user)

        return redirect('app:home')

    return render(request, 'auth/register.html')

