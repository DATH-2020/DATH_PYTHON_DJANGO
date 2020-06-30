from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.core.mail import send_mail  

admin.site.site_header ="Hệ thống quản lí thông tin HITECH"
admin.site.site_title ="Hệ thống quản lí thông tin HITECH"
admin.site.index_title = "HIETCH education"

admin.site.register(Gender)
admin.site.register(Area)
admin.site.register(Unit)
admin.site.register(TimeShift)
admin.site.register(TimeWeek)
admin.site.register(Room)
admin.site.register(Teacher)
admin.site.register(Schedule)
admin.site.register(CheckInClass)
admin.site.register(Classname)
admin.site.register(Student)
admin.site.register(Notify)