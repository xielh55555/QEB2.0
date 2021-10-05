from django.db import models

# Create your models here.



class Time(models.Model):       #TODO   上课时间
    name=models.CharField(max_length=12)
    def __str__(self):
        return self.name

class Classroom(models.Model):   #TODO 教室
    name=models.CharField(max_length=6)
    def __str__(self):
        return self.name

class Curriculum(models.Model):  #TODO  课程
    name=models.CharField(max_length=12)
    classroom=models.ForeignKey(Classroom,name='curriculum',on_delete=models.CASCADE)
    imgae=models.ImageField('照片',upload_to='img/',blank=True, null=True)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name=models.CharField(max_length=10,default=' ')
    curriculum=models.ManyToManyField(Curriculum,verbose_name='课程',default=' ',blank=True, null=True)
    imgae=models.ImageField('照片',upload_to='img/',blank=True, null=True)
    Number_of_classes=models.IntegerField(default=0)
    month=models.IntegerField(default=10)
    def __str__(self):
        return self.name



class Student(models.Model):
    SEX_G=(
        ('男','男生'),
        ('女','女生')
    )
    name=models.CharField(max_length=10)  # 名字，学号，年纪，姓别，上课时间，所在教室，课程，对应老师
    # student_id=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=2,choices=SEX_G)
    time=models.ForeignKey(Time,related_name='students',on_delete=models.CASCADE)
    classroom=models.ForeignKey(Classroom,related_name='students',on_delete=models.CASCADE)
    curriculum=models.ForeignKey(Curriculum,related_name='students',on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,related_name='students',on_delete=models.CASCADE)
    Remaining_lesson_J=models.IntegerField(default=0)
    def __str__(self):
        return self.name

