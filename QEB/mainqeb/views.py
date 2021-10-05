# from django.core import paginator
from django.shortcuts import render,get_object_or_404,redirect
from .models import Student, Teacher,Time,Classroom,Curriculum
from django.core.paginator import Paginator
import datetime
# from django.contrib import messages


#TODO Create your views here.
def check_login(func):
    def wrapper(*args,**kwargs):
        if not args[0].session.get('is_login'):
            return redirect('sign_in')
        return func(*args,**kwargs)
    return wrapper

@check_login
def home(request):
    return render(request,'home.html')

@check_login
def teacher(request):  
    teachers=Teacher.objects.all()    
    return render(request,'teacher.html',{'teachers':teachers})


@check_login
def teacher_classroom(request,teacher_id):  
    if request.method == 'POST':
        students=Student.objects.all()
        for student in students:
            if student.name in request.POST:
                student.Remaining_lesson_J-=1
                student.save()
                timetable=[
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]]
        ]
        timetable_image=[
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]]
        ]
        tim=['上午一','上午二','下午一','下午二','下午三','晚上']
        ti=['周三上午一','周三上午二','周三下午一','周三下午二','周三下午三','周三晚上',
        '周四上午一','周四上午二','周四下午一','周四下午二','周四下午三','周四晚上','周五上午一',
        '周五上午二','周五下午一','周五下午二','周五下午三','周五晚上','周六上午一','周六上午二',
        '周六下午一','周六下午二','周六下午三','周六晚上','周日上午一','周日上午二','周日下午一',
        '周日下午二','周日下午三','周日晚上']
        teacher=get_object_or_404(Teacher,pk=teacher_id)
        date=datetime.datetime.now().month
        if date == teacher.month:
            teacher.Number_of_classes+=1
            teacher.save()
            teacher_unmber_of_classes=teacher.Number_of_classes
        else:
            teacher.month=date           
            teacher.Number_of_classes=0
            teacher.save()
            teacher_unmber_of_classes=teacher.Number_of_classes
        teachers=Teacher.objects.all()
        students=Student.objects.filter(teacher=teacher.id)
        for student in students:
            for i in range(30):
                if student.time.name==ti[i]:
                    timetable[i%6][i//6].append(student.name)
                    timetable_image[i%6][i//6].append(Curriculum.objects.filter(name=student.curriculum))
        today = datetime.datetime.now().weekday() + 1
        timetable_list=[]
        timetable_image_list=[]
        for x in range(3,8):
            if today ==x:
                for i in range(6):
                    timetable_list.append(timetable[i][x-3])
                    timetable_image_list.append(timetable_image[i][x-3])
        return render(request,'teacher_classroom.html',{'teacher':teacher,
        'teachers':teachers,'teacher_unmber_of_classes':teacher_unmber_of_classes,'timetable_list':timetable_list,'timetable_image_list':timetable_image_list})
    else:      
        timetable=[
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]]
        ]
        timetable_image=[
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]]
        ]
        tim=['上午一','上午二','下午一','下午二','下午三','晚上']
        ti=['周三上午一','周三上午二','周三下午一','周三下午二','周三下午三','周三晚上',
        '周四上午一','周四上午二','周四下午一','周四下午二','周四下午三','周四晚上','周五上午一',
        '周五上午二','周五下午一','周五下午二','周五下午三','周五晚上','周六上午一','周六上午二',
        '周六下午一','周六下午二','周六下午三','周六晚上','周日上午一','周日上午二','周日下午一',
        '周日下午二','周日下午三','周日晚上']
        teacher=get_object_or_404(Teacher,pk=teacher_id)
        date=datetime.datetime.now().month
        if date == teacher.month:
            teacher_unmber_of_classes=teacher.Number_of_classes
        else:
            teacher.month=date           
            teacher.Number_of_classes=0
            teacher.save()
            teacher_unmber_of_classes=teacher.Number_of_classes
        teachers=Teacher.objects.all()
        students=Student.objects.filter(teacher=teacher.id)
        for student in students:
            for i in range(30):
                if student.time.name==ti[i]:
                    timetable[i%6][i//6].append(student.name)
                    timetable_image[i%6][i//6].append(Curriculum.objects.filter(name=student.curriculum))
        today = datetime.datetime.now().weekday() + 1
        timetable_list=[]
        timetable_image_list=[]
        for x in range(3,8):
            if today ==x:
                for i in range(6):
                    timetable_list.append(timetable[i][x-3])
                    timetable_image_list.append(timetable_image[i][x-3])
        return render(request,'teacher_classroom.html',{'teacher':teacher,
        'teachers':teachers,'teacher_unmber_of_classes':teacher_unmber_of_classes, 'timetable_list':timetable_list,'timetable_image_list':timetable_image_list})   

@check_login
def teacher_example(request,teacher_id):
    if request.method == 'POST':
        teacher=get_object_or_404(Teacher,pk=teacher_id)
        if teacher.students.all().count() == 0:
            teacher.delete()
            return redirect('home')
        else:
            messages_1='*请先移交学生到其他老师！' 
            timetable=[
                [[],[],[],[],[]],
                [[],[],[],[],[]],
                [[],[],[],[],[]],
                [[],[],[],[],[]],
                [[],[],[],[],[]],
                [[],[],[],[],[]]
            ]
            tim=['上午一','上午二','下午一','下午二','下午三','晚上']
            ti=['周三上午一','周三上午二','周三下午一','周三下午二','周三下午三','周三晚上',
            '周四上午一','周四上午二','周四下午一','周四下午二','周四下午三','周四晚上','周五上午一',
            '周五上午二','周五下午一','周五下午二','周五下午三','周五晚上','周六上午一','周六上午二',
            '周六下午一','周六下午二','周六下午三','周六晚上','周日上午一','周日上午二','周日下午一',
            '周日下午二','周日下午三','周日晚上']
            teacher=get_object_or_404(Teacher,pk=teacher_id)
            teachers=Teacher.objects.all()
            students=Student.objects.filter(teacher=teacher.id)
            leng=teacher.students.all().count()
            for student in students:
                for i in range(30):
                    if student.time.name==ti[i]:
                        timetable[i%6][i//6].append(student.name)
            return render(request,'teacher_example.html',{'teacher':teacher,'leng':leng,
            'teachers':teachers,'students':students,'timetable':timetable,'tim':tim,'messages_1':messages_1})
    else:
        timetable=[
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]],
            [[],[],[],[],[]]
        ]
        tim=['上午一','上午二','下午一','下午二','下午三','晚上']
        ti=['周三上午一','周三上午二','周三下午一','周三下午二','周三下午三','周三晚上',
        '周四上午一','周四上午二','周四下午一','周四下午二','周四下午三','周四晚上','周五上午一',
        '周五上午二','周五下午一','周五下午二','周五下午三','周五晚上','周六上午一','周六上午二',
        '周六下午一','周六下午二','周六下午三','周六晚上','周日上午一','周日上午二','周日下午一',
        '周日下午二','周日下午三','周日晚上']
        teacher=get_object_or_404(Teacher,pk=teacher_id)
        teachers=Teacher.objects.all()
        students=Student.objects.filter(teacher=teacher.id)
        leng=teacher.students.all().count()
        for student in students:
            for i in range(30):
                if student.time.name==ti[i]:
                    timetable[i%6][i//6].append(student.name)
        return render(request,'teacher_example.html',{'teacher':teacher,'leng':leng,
        'teachers':teachers,'students':students,'timetable':timetable,'tim':tim})

@check_login
def student(request):
    if request.method == 'POST':
        if 'search' in request.POST:
            q=request.POST.get('q')
            error_msg= ''
            if not q:
                error_msg='请输入关键词'
                return render(request,'student.html',{'error_msg':error_msg})
            post_list=Student.objects.filter(name=q)
            limit=18
            paginator=Paginator(post_list,limit)
            page=request.GET.get('page','1')
            result=paginator.page(page)
            return render(request,'student.html',{ 'students':result})
        elif 'add' in request.POST:
            return redirect('student_add')
        elif 'warning' in request.POST:
            students=Student.objects.all()
            students_num=len(students)
            student_list=[]
            for student in students:
                if student.Remaining_lesson_J <10:
                    student_list.append(student)
            students=student_list
            return render(request,'student.html',{'students':students,'students_num':students_num})       
    else:
        students=Student.objects.all()
        students_num=len(students) 
        limit=18
        paginator=Paginator(students,limit)
        page=request.GET.get('page','1')
        result=paginator.page(page)
        page=int(page)
        if page==1 or page=='':
            page=1
            return render(request,'student.html',{ 'students':result,
            'students_num':students_num,'page':page})
        else:
            return render(request,'student.html',{ 'students':result,
            'students_num':students_num,'page':page})


@check_login
def student_example(request,student_id):
    if request.method =='POST':
        if  'determine' in request.POST:
            try:
                personal_information_name=request.POST['name']
                personal_information_age=request.POST['age']
                personal_information_gender=request.POST['gender']
                personal_information_time=request.POST['time']
                personal_information_classroom=request.POST['classroom']
                personal_information_curriculum=request.POST['curriculum']
                personal_information_teacher=request.POST['teacher']
                personal_information_Remaining_lesson_J=request.POST['Remaining_lesson_J']
                student=Student.objects.get(name=personal_information_name)
                student.age=personal_information_age
                student.gender=personal_information_gender
                student.time=Time.objects.get(name=personal_information_time)    
                student.classroom=Classroom.objects.get(name=personal_information_classroom)
                student.curriculum=Curriculum.objects.get(name=personal_information_curriculum)
                student.teacher=Teacher.objects.get(name=personal_information_teacher)
                student.Remaining_lesson_J=personal_information_Remaining_lesson_J
                student.save()
                return render(request,'student_example.html',{'student':student})
            except:
                student=get_object_or_404(Student,pk=student_id)
                times=Time.objects.all()  
                classrooms=Classroom.objects.all() 
                curriculums=Curriculum.objects.all()  
                teachers=Teacher.objects.all()  
                messages_1='*为必填内容！' 
                return render(request,'student_example.html',{'student':student,'messages_1':messages_1,
                'teachers':teachers,'curriculums':curriculums,'classrooms':classrooms,'times':times})
        elif 'delete' in request.POST:
            try:
                personal_information_name=request.POST['name']
                student=Student.objects.get(name=personal_information_name)
                student.delete()
                students=Student.objects.all()
                limit=18
                paginator=Paginator(students,limit)
                page=request.GET.get('page','1')
                result=paginator.page(page)
                return render(request,'student.html',{ 'students':result})
            except:
                student=get_object_or_404(Student,pk=student_id)
                times=Time.objects.all()  
                classrooms=Classroom.objects.all() 
                curriculums=Curriculum.objects.all()  
                teachers=Teacher.objects.all()  
                messages_1='*该生不在本校！' 
                return render(request,'student_example.html',{'student':student,'messages_1':messages_1,
                'teachers':teachers,'curriculums':curriculums,'classrooms':classrooms,'times':times})
        else:
            pass
    else:
        student=get_object_or_404(Student,pk=student_id)
        times=Time.objects.all()  
        classrooms=Classroom.objects.all() 
        curriculums=Curriculum.objects.all()  
        teachers=Teacher.objects.all()  
        return render(request,'student_example.html',{'student':student,
        'teachers':teachers,'curriculums':curriculums,'classrooms':classrooms,'times':times})


@check_login
def text(request):
    return render(request,'text.html')        


@check_login
def student_add(request):
    if  request.method =='POST':
        try:
            name=request.POST['name']
            age=request.POST['age']
            gender=request.POST['gender']
            time=Time.objects.get(name=request.POST['time'])
            classroom=Classroom.objects.get(name=request.POST['classroom'])
            curriculum=Curriculum.objects.get(name=request.POST['curriculum'])
            teacher=Teacher.objects.get(name=request.POST['teacher'])
            Remaining_lesson_J=request.POST['Remaining_lesson_J']
            student=Student.objects.create(name=name,age=age,gender=gender,
            time=time,classroom=classroom,curriculum=curriculum,teacher=teacher,
            Remaining_lesson_J=Remaining_lesson_J)
            student.save()
            students=Student.objects.all()
            limit=18
            paginator=Paginator(students,limit)
            page=request.GET.get('page','1')
            result=paginator.page(page)
            return render(request,'student.html',{ 'students':result})
        except :
            times=Time.objects.all()  
            classrooms=Classroom.objects.all() 
            curriculums=Curriculum.objects.all()  
            teachers=Teacher.objects.all() 
            messages_1='*为必填内容！' 
            return render(request,'student_add.html',{'teachers':teachers,
            'curriculums':curriculums,'classrooms':classrooms,'times':times,'messages_1':messages_1})
    else:
        times=Time.objects.all()  
        classrooms=Classroom.objects.all() 
        curriculums=Curriculum.objects.all()  
        teachers=Teacher.objects.all() 
        return render(request,'student_add.html',{'teachers':teachers,
        'curriculums':curriculums,'classrooms':classrooms,'times':times})

