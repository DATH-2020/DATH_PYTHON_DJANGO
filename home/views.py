from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

from .models import *
from .forms import CreateUserForm, CreateStudentForm
# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user )
                return redirect('home')
            else:
                messages.into(request, 'Tên đăng nhập hoặc mật khẩu không đúng')
                return render(request, 'pages/login.html', context)
        context={}
        return render(request, 'pages/login.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()  
                user = form.cleaned_data.get('username')
                messages.into(request, 'Tài khoản ' + user + ' đã tồn tại')
                return redirect()

        context = {'form':form}
        return render(request, 'pages/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
    
@login_required(login_url='login')
def home(request):
    return render(request, 'pages/home.html')

# Class 
# Dat
@login_required(login_url='login')
def listClass(request):
    listclass = Classname.objects.all()
    context = {'listclass': listclass}
    return render(request, 'class/listclass.html', context)

@login_required(login_url='login')
def createClass(request):
    context = {}
    return render(request, 'class/createClass.html', context)

# Student 
# Dat
@login_required(login_url='login')
def listStudent(request):
    liststudent = Student.objects.all()
    context = {'liststudent': liststudent}
    return render(request, 'student/student.html', context)
    
@login_required(login_url='login')
def createStudent(request):
    form = CreateStudentForm()
    gender = Gender.objects.all()
    unit = Unit.objects.all()
    classname = Classname.objects.all()
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                subject = 'Xác nhận đăng kí học viên', # title mail
                message = 'Bạn vừa hoàn thành đăng kí học viên tại HITECH, vui lòng kiểm tra nếu nội dung không chính xác. Xin cảm ơn !', # nội dung mail
                from_email= None, # tài khoản
                auth_password= None, # mk
                recipient_list = [form.cleaned_data.get('email')],# mail người nhận
                fail_silently = False,
            )
            return redirect('liststudent')
    context = {'form':form, 'gender':gender, 'unit':unit, 'classname':classname}
    return render(request, 'student/createStudent.html', context)

# Teacher 
# Dat
@login_required(login_url='login')
def listTeacher(request):
    listteacher = Teacher.objects.all()
    context = {'listteacher': listteacher}
    return render(request, 'teacher/teacher.html', context)
 