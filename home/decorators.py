from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User

from .models import *

def unauthenticated_register(view_func):
    def wrapper_func(request, *args, **kwargs):
        a = User.objects.all().count()
        if a > 1:
            return redirect('login')
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def unauthenticated_login(view_func):
    def wrapper_func(request, *args, **kwargs):
        a = User.objects.all().count()
        if a == 1:
            return redirect('register')
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs) 
    return wrapper_func
  
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('errorrole')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        if group == 'manager':
            return redirect('errorrole')
    return wrapper_func