from django.db import models

# Create your models here.

class Gender(models.Model):
    name = models.CharField(max_length=5, verbose_name="Giới tính")

    def __str__(self):
        return  self.name
    class Meta:
        ordering =["name"]
        verbose_name_plural = "Giới tính"

class Area(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Tên cơ sở")
    phonenumber = models.CharField(max_length=100, null=True, blank=True, default="", verbose_name="SDT")
    email = models.CharField(max_length=100, null=True, blank=True, default="", verbose_name="Email")
    adress = models.CharField(max_length=300, null=True, blank=True, default="", verbose_name="Địa chỉ")
    note = models.CharField(max_length=300, null=True, blank=True, default="", verbose_name="Ghi chú")
    active = models.BooleanField(default=True, verbose_name="Trạng thái")

    def __str__(self):
        return  self.fullname
    class Meta:
        ordering =["fullname"]
        verbose_name_plural = "Chi nhánh"

class Unit(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Tên khóa học")
    infomation = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Thông tin khóa học")
    fee = models.IntegerField(default=0, verbose_name="Học phí khóa học")
    active = models.BooleanField(default=True, verbose_name="Trạng thái")

    def __str__(self):
        return  self.fullname
    class Meta:
        ordering =["fullname"]
        verbose_name_plural = "Khóa học"

class TimeShift(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Tên ca học")
    infomation = models.CharField(max_length=1000, blank=True, verbose_name="Thông tin ca học")
    timestart = models.TimeField(null = True, blank=True, verbose_name="Giờ bắt đầu")
    timeend = models.TimeField(null = True, blank=True, verbose_name="Giờ kết thúc")
    active = models.BooleanField(default=True, verbose_name="Trạng thái")
    
    def __str__(self):
        return  self.fullname
    class Meta:
        ordering =["fullname"]
        verbose_name_plural = "Ca học"

class TimeWeek(models.Model):
    name = models.CharField(max_length=100, verbose_name="Loại")

    def __str__(self):
        return  self.name
    class Meta:
        ordering =["name"]
        verbose_name_plural = "Ngày học trong tuần"

class Room(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Tên phòng")
    area = models.ForeignKey(Area, null= True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True, verbose_name="Trạng thái")

    def __str__(self):
        return  self.fullname
    class Meta:
        ordering =["fullname"]
        verbose_name_plural = "Phòng"

class Teacher(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Tên giáo viên")
    gender = models.ForeignKey(Gender, null= True, on_delete=models.SET_NULL)
    birthday = models.DateField(verbose_name="Ngày sinh")
    identity_card = models.CharField(max_length=100, null = True, blank=True, verbose_name="CMND")
    phonenumber = models.CharField(max_length=100, null = True, blank=True, verbose_name="SDT")
    email = models.CharField(max_length=100, null = True, blank=True, verbose_name="Email")
    adress = models.CharField(max_length=300, null = True, blank=True, verbose_name="Địa chỉ")
    create_date = models.DateField(auto_now_add=True, verbose_name="Ngày tạo thông tin")
    note = models.CharField(max_length=300, null = True, blank=True, verbose_name="Ghi chú")
    active = models.BooleanField(default=True, verbose_name="Trạng thái")

    def __str__(self):
        return  self.fullname
    class Meta:
        ordering =["fullname"]
        verbose_name_plural = "Giáo viên"

class Classname(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Tên lớp học")
    startdate = models.DateField(auto_now_add=True, verbose_name="Ngày bắt đầu")
    room = models.ForeignKey(Room, null= True, on_delete=models.SET_NULL)
    unit = models.ForeignKey(Unit, null = True, on_delete=models.SET_NULL)
    timeshift = models.ForeignKey(TimeShift, null = True, on_delete=models.SET_NULL)
    startdate = models.DateField(verbose_name="Ngày bắt đầu học")
    timeweek = models.ForeignKey(TimeWeek, null = True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, null = True, on_delete=models.SET_NULL)
    datecount = models.IntegerField(default=0, blank=True, verbose_name="Số buổi học")
    note = models.CharField(max_length=300, null = True, blank=True, verbose_name="Ghi chú")
    active = models.BooleanField(default=True, verbose_name="Trạng thái")

    def __str__(self):
        return  self.fullname
    class Meta:
        ordering =["fullname"]
        verbose_name_plural = "Lớp học"
                
class Student(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Tên học sinh")
    gender = models.ForeignKey(Gender, null= True, on_delete=models.SET_NULL)
    birthday = models.DateField(verbose_name="Ngày sinh")
    identity_card = models.CharField(max_length=100, null = True, blank=True, verbose_name="CMND")
    phonenumber = models.CharField(max_length=100, null = True, blank=True, verbose_name="SDT")
    phonenumber_family = models.CharField(max_length=100, null = True, blank=True, verbose_name="SDT phụ huynh")
    email = models.CharField(max_length=100, null = True, blank=True, verbose_name="Email")
    adress = models.CharField(max_length=300, null = True, blank=True, verbose_name="Địa chỉ")
    classname = models.ForeignKey(Classname, null= True, on_delete=models.SET_NULL)
    fee = models.IntegerField(default=0, verbose_name="Học phí")
    fee_remain = models.IntegerField(default=0, verbose_name="Học phí còn lại")
    create_date = models.DateField(auto_now_add=True, verbose_name="Ngày đăng ký học")
    havedetailschedule = active = models.BooleanField(default=False, verbose_name="Thời khóa biểu cá nhân")
    note = models.CharField(max_length=300, null = True, blank=True, verbose_name="Ghi chú")
    active = models.BooleanField(default=True, verbose_name="Trạng thái")

    def __str__(self):
        return  self.fullname
    class Meta:
        ordering =["fullname"]
        verbose_name_plural = "Học sinh"

class Schedule(models.Model):
    id_classname = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID học viên")
    classname = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tên lớp")
    dayname = models.CharField(max_length=50, blank=True, null=True, verbose_name="Buổi")
    daylearn = models.DateField(verbose_name="Ngày học")
    timelearnstart = models.TimeField(null = True, blank=True,verbose_name="Thời gian học")
    timelearnend = models.TimeField(null = True, blank=True,verbose_name="Thời gian kết thúc")
    note = models.CharField(max_length=300, null = True, blank=True, verbose_name="Ghi chú")
    active = models.BooleanField(default=True, verbose_name="Trạng thái")
    
    def __str__(self):
        return  self.classname
    class Meta:
        ordering =["classname"]
        verbose_name_plural = "Lịch học theo lớp"

class CheckInClass(models.Model):
    id_student = models.IntegerField(default=0, blank=True, null=True, verbose_name="ID học viên")
    student = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tên học viên")
    classname = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tên lớp")
    dayname = models.CharField(max_length=50, blank=True, null=True, verbose_name="Buổi")
    daylearn = models.DateField(verbose_name="Ngày học")
    timelearnstart = models.TimeField(null = True, blank=True,verbose_name="Thời gian học")
    timelearnend = models.TimeField(null = True, blank=True,verbose_name="Thời gian kết thúc")
    note = models.CharField(max_length=300, null = True, blank=True, verbose_name="Ghi chú")
    active = models.BooleanField(default=True, verbose_name="Trạng thái")
    
    def __str__(self):
        return  self.student
    class Meta:
        ordering =["student"]
        verbose_name_plural = "Thời khóa biểu cá nhân"

class Notify(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tiêu đề")
    content = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Nội dung")
    create_date = models.DateField(auto_now_add=True, verbose_name="Ngày đăng")
    active = models.BooleanField(default=True, verbose_name="Trạng thái")

    def __str__(self):
        return  self.title
    class Meta:
        ordering =["title"]
        verbose_name_plural = "Thông báo"