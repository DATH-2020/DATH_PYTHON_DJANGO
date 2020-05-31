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
from django.contrib.auth.models import Group

from .models import *
from .forms import *
from .decorators import *
# Create your views here.
@unauthenticated_user
def loginPage(request):
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

@unauthenticated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()  
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='manager')
                user.group.add(group)

                messages.success(request, 'Tài khoản ' + username + ' tạo thành công')
                return redirect('login')
            else:
                messages.error(request, "Lỗi tạo tài khoản")
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
    unit = Unit.objects.all()
    area = Area.objects.all()
    room = Room.objects.all()
    timeshift = TimeShift.objects.all()
    timeweek = TimeWeek. objects.all()
    teacher = Teacher.objects.all()
    form = UpdateClassForm(instance=classname)
    if request.method == 'POST':
        form = UpdateClassForm(request.POST, instance=classname)
        if form.is_valid():
            form.save()
            return redirect('listclass')
    context={'form':form, 'classname':classname, 'unit':unit, 'area':area, 'room':room, 'timeshift':timeshift, 'timeweek':timeweek, 'teacher':teacher}
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
    
@login_required(login_url='login')
def createTeacher(request):
    gender = Gender.objects.all()
    listteacher = Teacher.objects.all()
    form = CreateTeacherForm()
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listteacher')
    context = {'form':form, 'listteacher': listteacher, 'gender':gender}
    return render(request, 'teacher/createTeacher.html', context)

@login_required(login_url='login')
def detailTeacher(request,pk):
    teacher = Teacher.objects.get(pk=pk)
    gender = Gender.objects.all()
    form = UpdateTeacherForm(instance=teacher)
    if request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('listteacher')
    context = {'form':form, 'teacher':teacher, 'gender': gender}
    return render(request,'teacher/detailTeacher.html',context)

# Manager 
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def listStaf(request):
    context={}
    return render(request,'manager/staf.html',context)

# Contact 
@login_required(login_url='login')
def contact(request):
    return render(request,'contact/contact.html')
 