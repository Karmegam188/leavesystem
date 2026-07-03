from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User


def home(request):
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        return redirect('login')

    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # 🔥 Role-based redirect
            if user.role == 'admin':
                return redirect('/admin/')
            elif user.role == 'manager':
                return redirect('/leave/manager/')
            else:
                return redirect('/leave/employee/')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')