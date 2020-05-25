from django.urls import path
from .import views

urlpatterns = [
    path('',views.StudentListView, name='liststudent'),
    #path('<int:pk>/',views.StudentDetailView.as_view(), name='detailstudent'),
    path('<int:pk>/',views.DetailStudent,name='detailstudent'),
    path('create/',views.CreateStudent,name='create'),
    path('upload/',views.upload_file,name='upload'),
    path('base2/',views.test, name='test'),
    path('class/',views.ListClass.as_view(),name='listclass')

]