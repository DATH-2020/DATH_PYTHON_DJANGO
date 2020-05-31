from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CreateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class UpdateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = 'email','phonenumber','adress','phonenumber_family','classname','fee','fee_remain','note','active'

class CreateClassnameForm(ModelForm):
    class Meta:
        model = Classname
        fields = '__all__'
        
class UpdateClassForm(ModelForm):
    class Meta:
        model = Classname
        fields = 'teacher','timeshift','timeweek','room','startdate','note','active'

class CreateTeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class UpdateTeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = 'email','phonenumber','adress','note','active'