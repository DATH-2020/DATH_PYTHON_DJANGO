from django.urls import path
from .import views

urlpatterns = [
    path('',views.ListStudent, name='liststudent'),
    #path('<int:pk>/',views.StudentDetailView.as_view(), name='detailstudent'),
    # path('<int:pk>/',views.DetailStudent,name='detailstudent'),
    path('upload/',views.upload_file,name='upload'),
    path('base2/',views.test, name='test'),
    # path('class/',views.ListClass,name='listclass'),
    # Class 
    path('createclass/',views.CreateClass,name='createclass'),
    path('listclass/',views.ListClass,name='listclass'),
    path('detailclass/',views.DetailClass,name='detailclass'),
    # Contact 
    path('contact/',views.Contact,name='contacts'),
    # Manager 
    path('createstafaccount/',views.CreateStafAccount,name='createstafaccount'),
    path('liststaf/',views.ListStaf,name='liststaf'),
    path('roleacount/',views.RoleAcount,name='roleacount'),
    # Schedule 
    path('createschedule/',views.CreateSchedule,name='createschedule'),
    path('listschedule/',views.ListSchedule,name='listschedule'),
    path('detailschedule/',views.DetailSchedule,name='detailschedule'),
    # Student 
    path('create/',views.CreateStudent,name='create'),
    # path('liststudent/',views.ListStudent,name='liststudent'),
    path('<int:pk>/',views.DetailStudent,name='detailstudent'),
    # Teacher 
    path('createteacher/',views.CreateTeacher,name='createteacher'),
    path('listteacher/',views.ListTeacher,name='listteacher'),
    path('detailteacher/',views.DetailTeacher,name='detailteacher'),
    
]