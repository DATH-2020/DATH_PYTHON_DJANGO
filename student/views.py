from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from student.models import Student,Classes,StudentInClass,MyUser
from .forms import CreationForm,TimeStudentForm,UploadFileForm
from django.views.generic import ListView, DetailView
import openpyxl
# Create your views here.
class StudentListView(ListView): 
    queryset = Student.objects.all()
    template_name = 'student/student.html'
    context_object_name = 'Students' # đặt tên truyền vào Temp
    paginate_by = 10  #phân trang
#class StudentDetailView(DetailView): # Trang info student
   # model = Student
   # template_name = 'student/detailStudent.html'
def DetailStudent(request,pk):
    student = get_object_or_404(Student,pk=pk) # chỉ định tham số pk 
    
    #form = TimeStudentForm()
    return render(request, 'student/detailStudent.html', {'student':student,} )

def CreateStudent(request):
    form = CreationForm()
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/student")
        return HttpResponse("Dữ liệu không hợp lệ")
    return render(request, 'student/createStudent.html', {'form':form})
              
def upload_file(request):
    if request.method == 'POST' and request.user.is_staff == True and request.user.is_superuser == False:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']

            # you may put validations here to check extension or file size
            wb = openpyxl.load_workbook(excel_file)

            # lấy dữ liệu từ "Sheet1" không phải "Sheet2" hay là "Sheet11"
            worksheet = wb["Sheet1"]
            print(worksheet)

            excel_data = list()
            # iterating over the rows and
            # getting value from each cell in row
            user = MyUser.objects.get(user=request.user)
            for row in worksheet.iter_rows():
                row_data = list()
                for cell in row:
                    row_data.append(str(cell.value))
                Student.objects.create(name=row_data[0],phone_number_1=row_data[1],learning_area=user.area)
            return render(request, 'pages/Success.html',{"excel_data":excel_data})
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request, 'student/upload.html', {'form': form})

def test(request):
    return render(request,'pages/base2.html', {'form': form})
