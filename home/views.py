from django.shortcuts import render
from .forms import RegistrationForm
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from student.forms import CreationForm
from django.http import HttpResponseRedirect,HttpResponse
from blog.models import Post
from student.models import Area
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
# Login
# Dat
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student')
    context = {}
    return render(request, 'pages/login.html')
# def index(request):
#     area=Area.objects.all()
#     form = CreationForm()
#     #post= Post.objects.all().order_by("-date")
#     #paginator = Paginator(post,4)
#     #page = request.GET.get('page')
#     #contacts = paginator.get_page(page)

#     if request.method == 'POST':
#         form = CreationForm(request.POST)
#         alert=False
#         if form.is_valid():
#             form.save()
#             alert=True
#             return render(request, 'pages/home.html',{'area':area,'alert':alert})#,'post':contacts})
#         return HttpResponse("Dữ liệu không hợp lệ")
#     return render(request, 'pages/home.html', {'area':area,'form':form})#, 'post':contacts})
def contact(request):
    return render(request, 'pages/contact.html')
def error(request):
    return render(request, 'pages/error.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form =RegistrationForm(request.POST)
        if form.is_valid(): # gọi các hàm có clean_ ở đầu tiên
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html',{'form':form})
