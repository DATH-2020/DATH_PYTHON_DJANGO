from django import forms
import re
from .models import Student,StudentInClass

class UploadFileForm(forms.Form):
    file = forms.FileField()
    # def clean_file(self):
    #     if self.file

class CreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name',None)
        self.phone_number_1 = kwargs.pop('phonenum1',None)
        self.learning_area = kwargs.get('area',None)
        super().__init__(*args, **kwargs)
    class Meta:
        model = Student
        Student.is_learning=False
        fields = ["name","phone_number_1","learning_area"]
    
class TimeStudentForm(forms.ModelForm):
    class Meta:
        model = StudentInClass
        fields = ["class_id"]


