from django.contrib import admin

# Register your models here.
from .models import Teacher,Classroom,Curriculum,Time,Student

admin.site.register(Time)
admin.site.register(Teacher)
admin.site.register(Curriculum)
admin.site.register(Student)
admin.site.register(Classroom)