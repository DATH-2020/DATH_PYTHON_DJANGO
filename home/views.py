from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.http import Http404

from .models import *
from .forms import *
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
                messages.info(request, 'Tên đăng nhập hoặc mật khẩu không đúng')
                return render(request, 'pages/login.html')
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
                messages.success(request, 'Tài khoản ' + user + ' tạo thành công')
                return redirect('login')
            else:
                messages.error(request, "Lỗi đăng ký")
                return render(request, 'pages/register.html')
        context = {}
        return render(request, 'pages/register.html')
        # context = {'form':form}
        # return render(request, 'pages/register.html', context)

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
    form = CreateClassnameForm()
    unit = Unit.objects.all()
    area = Area.objects.all()
    room = Room.objects.all()
    timeshift = TimeShift.objects.all()
    timeweek = TimeWeek. objects.all()
    teacher = Teacher.objects.all()
    if request.method == 'POST':
        form = CreateClassnameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listclass')
    context = {'form':form, 'unit':unit, 'area':area, 'room':room, 'timeshift':timeshift, 'timeweek':timeweek, 'teacher':teacher}
    return render(request, 'class/createClass.html', context)

@login_required(login_url='login')
def detailClass(request,pk):
    classname = Classname.objects.get(pk=pk)
    context={'classname':classname}
    return render(request,'class/detailClass.html',context)

# Student 
# Dat
@login_required(login_url='login')
def listStudent(request):
    form = CreateStudentForm()
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
    context = { 'gender':gender, 'unit':unit, 'classname':classname}
    return render(request, 'student/createStudent.html', context)

@login_required(login_url='login')
def detailStudent(request,pk):
    student = Student.objects.get(pk=pk)
    classname = Classname.objects.all()
    unit = Unit.objects.all()
    form = UpdateStudentForm(instance=student)
    if request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            send_mail(
                subject = 'Xác nhận đã cập nhật lại thông tin học viên', # title mail
                message = 'Bạn vừa hoàn thành cập nhật thông tin học viên tại HITECH, vui lòng kiểm tra nếu nội dung không chính xác. Xin cảm ơn !', # nội dung mail
                from_email= None, # tài khoản
                auth_password= None, # mk
                recipient_list = [form.cleaned_data.get('email')],# mail người nhận
                fail_silently = False,
            )
            return redirect('liststudent')
    context = {'form':form, 'student':student, 'classname': classname, 'unit': unit}
    return render(request,'student/detailStudent.html',context)

# Teacher 
# Dat
@login_required(login_url='login')
def listTeacher(request):
    listteacher = Teacher.objects.all()
    context = {'listteacher': listteacher}
    return render(request, 'teacher/teacher.html', context)

# Manager 
@login_required(login_url='login')
def listStaf(request):
    context={}
    return render(request,'manager/staf.html',context)

# Contact 
@login_required(login_url='login')
def contact(request):
    return render(request,'contact/contact.html')
 