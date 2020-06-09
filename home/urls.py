from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name="pages/changePassSuccess.html"), name="password_change_done"),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name="pages/changePassword.html"), name="change_password"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="pages/password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="pages/sendEmailSuccess.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="pages/newPassword.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="pages/resetPassSuccess.html"), name="password_reset_complete"),

    path('', views.home, name="home"),

    # # Class 
    path('listclass/', views.listClass, name='listclass'),
    path('createclass/', views.createClass, name='createclass'),
    path('class/<int:pk>/', views.detailClass, name='detailclass'),
    path('classstudent/<int:pk>/', views.detailClassStudent, name='detailclassstudent'),
    path('checkinclassstudent/<int:pk>/', views.checkinClassStudent, name='checkinclassstudent'),

    # # Manager 
    path('createstafaccount/',views.createStafAccount,name='createstafaccount'),
    path('updateuser/<int:pk>',views.updateUser,name='updateuser'),
    path('editprofile/<str:pk>',views.editProfile,name='editprofile'),
    path('listuser/',views.listUser,name='listuser'),
    path('newroom/',views.newRoom,name='newroom'),
    path('editroom/<int:pk>',views.editRoom,name='editroom'),
    path('newarea/',views.newArea,name='newarea'),
    path('editarea/<int:pk>',views.editArea,name='editarea'),
    path('listarea/',views.listArea,name='listarea'),
    path('notify/',views.notify,name='notify'), 
    path('editnotify/<int:pk>',views.editNotify,name='editnotify'), 
    path('createtimeshift/',views.createTimeShift,name='createtimeshift'), 
    path('edittimeshift/<int:pk>',views.editTimeShift,name='edittimeshift'),
    path('createunit/',views.createUnit,name='createunit'), 
    path('editinformationunit/<int:pk>',views.editInformationUnit,name='editinformationunit'),
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
    path('errorrole/',views.errorRole, name='errorrole'),

]