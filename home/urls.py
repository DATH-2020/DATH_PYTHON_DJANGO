from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),

    # # Class 
    path('listclass/', views.listClass, name='listclass'),
    path('createclass/', views.createClass, name='createclass'),
    path('class/<int:pk>/', views.detailClass, name='detailclass'),
    path('classstudent/<int:pk>/', views.detailClassStudent, name='detailclassstudent'),

    # # Manager 
    # path('createstafaccount/',views.CreateStafAccount,name='createstafaccount'),
    path('liststaf/',views.listStaf,name='liststaf'),
    # path('roleacount/',views.RoleAcount,name='roleacount'),
    # # Schedule 
    # path('createschedule/',views.CreateSchedule,name='createschedule'),
    # path('listschedule/',views.ListSchedule,name='listschedule'),
    # path('detailschedule/',views.DetailSchedule,name='detailschedule'),
    # Student 
    path('checkinstudent/<int:pk>/', views.checkinStudent, name='checkinstudent'),
    path('liststudent/', views.listStudent, name='liststudent'),
    path('createstudent', views.createStudent, name='createstudent'),
    path('student/<int:pk>/',views.detailStudent,name='detailstudent'),
    # path('createdetailschedule/<int:pk>/',views.createDetailSchedule,name='createdetailschedule'), 
    # # Teacher 
    path('createteacher/',views.createTeacher,name='createteacher'),
    path('listteacher/',views.listTeacher,name='listteacher'),
    path('teacher/<int:pk>/',views.detailTeacher,name='detailteacher'),

    path('contact/',views.contact, name='contact'),
]