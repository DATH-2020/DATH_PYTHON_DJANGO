from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2','is_staff','is_superuser','is_active']

class CreateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class UpdateStudentForm(ModelForm):
    class Meta:
        model = Student 
        fields = 'email','phonenumber','adress','phonenumber_family','fee','fee_remain','note','active'

class CreateClassnameForm(ModelForm):
    class Meta:
        model = Classname
        fields = '__all__'
        
class UpdateClassForm(ModelForm):
    class Meta:
        model = Classname
        fields = 'teacher','note','active'

class CreateTeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class UpdateTeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = 'email','phonenumber','adress','note','active'

class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class CreateAreaForm(ModelForm):
    class Meta:
        model = Area
        fields = '__all__'
        
class CreateNotifyForm(ModelForm):
    class Meta:
        model = Notify
        fields = '__all__'     

class CreateTimeShiftForm(ModelForm):
    class Meta:
        model = TimeShift
        fields = '__all__'

class CreateUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'