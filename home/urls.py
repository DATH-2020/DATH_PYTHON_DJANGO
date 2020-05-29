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
    # path('listclass/',views.ListClass,name='listclass'),
    # path('detailclass/',views.DetailClass,name='detailclass'),
    # # Contact 
    # path('contact/',views.Contact,name='contacts'),
    # # Manager 
    # path('createstafaccount/',views.CreateStafAccount,name='createstafaccount'),
    # path('liststaf/',views.ListStaf,name='liststaf'),
    # path('roleacount/',views.RoleAcount,name='roleacount'),
    # # Schedule 
    # path('createschedule/',views.CreateSchedule,name='createschedule'),
    # path('listschedule/',views.ListSchedule,name='listschedule'),
    # path('detailschedule/',views.DetailSchedule,name='detailschedule'),
    # Student 
    path('liststudent/', views.listStudent, name='liststudent'),
    path('createstudent', views.createStudent, name='createstudent'),
    # path('<int:pk>/',views.DetailStudent,name='detailstudent'),
    # # Teacher 
    # path('createteacher/',views.CreateTeacher,name='createteacher'),
    path('listteacher/',views.listTeacher,name='listteacher'),
    # path('detailteacher/',views.DetailTeacher,name='detailteacher'),
]