from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import CustomUserModel
from .forms import CustomUserForm
from .forms import CustomUserRegisterForm



def login_view(request):
    if request.method == 'POST':
        form = CustomUserForm(data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('conspect:home')
    form = CustomUserForm()
    return render(request, 'login.html', {'form': form,
                                          })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('conspect:home')
    return render(request, 'logout.html', {})


def user_register_view(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:register')
    form = CustomUserRegisterForm()
    return render(request, 'registration.html', {'form': form, })
















