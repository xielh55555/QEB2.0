from django.urls import path,re_path
from mainqeb import views


urlpatterns = [
    path('',views.home,name='home'),
    path('teacher/',views.teacher,name='teacher'),
    path('teacher/classroom/<int:teacher_id>/',views.teacher_classroom,name='teacher_classroom'),
    path('teacher/<int:teacher_id>/',views.teacher_example,name='teacher_example'),
    path('student/',views.student,name='student'),
    path('student/<int:student_id>/',views.student_example,name='student_example'),
    path('text/',views.text,name='text'),
    path('student/add/',views.student_add,name='student_add'),
    
    

   
]