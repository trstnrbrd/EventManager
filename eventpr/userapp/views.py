from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


def user(request):
    if request.method == 'POST':
        username        = request.POST.get('username', '').strip()
        email           = request.POST.get('email', '').strip()
        password        = request.POST.get('password', '')
        confirmpassword = request.POST.get('confirmpassword', '')

        if password != confirmpassword:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "That username is already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with that email already exists.")
            return redirect('register')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created! Please log in.")
        return redirect('login')

    return render(request, 'reg.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user_obj = auth.authenticate(request, username=username, password=password)

        if user_obj is not None:
            auth.login(request, user_obj)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'log.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
