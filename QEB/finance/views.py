from django.shortcuts import get_object_or_404, redirect, render
from .models import Expenditure,Income
import datetime
# Create your views here.


def finance(request):   
    year=datetime.datetime.now().year
    expenditures=Expenditure.objects.filter(year=year)
    incomes=Income.objects.filter(year=year)
    expenditure_total_list=[0,0,0,0,0,0,0,0,0,0,0,0]     #TODO   支出合集
    income_total_list=[0,0,0,0,0,0,0,0,0,0,0,0]          #TODO   收入合集
    totalall_list=[0,0,0,0,0,0,0,0,0,0,0,0]              #TODO   节余合集
    expenditure_total=0                                  #TODO   支出合计
    income_total=0                                       #TODO   收入合计
    for expenditure in expenditures:
        for i in range(12):
            if expenditure.month ==(i+1):
                expenditure_total_list[i]+=expenditure.money
    for income in incomes:
        for i in range(12):
            if income.month ==(i+1):
                income_total_list[i]+=income.money
    for i in range(12):
        totalall_list[i]=round(income_total_list[i] - expenditure_total_list[i],2)
    for x in expenditure_total_list:
        expenditure_total+=x
    for x in income_total_list:
        income_total+=x
    totalall=income_total-expenditure_total
    return render(request,'finance.html',{'expenditure_total_list':expenditure_total_list,'year':year,
    'income_total_list':income_total_list,'totalall_list':totalall_list,
    'expenditure_total':expenditure_total,'income_total':income_total,'totalall':totalall})


def expenditure(request):
    if request.method =='POST':
        if  'search' in request.POST:
            year=request.POST.get('year')
            month=request.POST.get('month')
            error_msg= ''
            if not month:
               error_msg='请输入关键词'
               return render(request,'expenditure.html',{'error_msg':error_msg})
            expenditures=Expenditure.objects.filter(month=month,year=year)
            total=0
            for expenditure in expenditures:
                total+=expenditure.money
            return render(request,'expenditure.html',{'total':total,'year':year,
            'month':month,'expenditures':expenditures})
        if 'add' in request.POST:
            return redirect('expenditure_add')
    else:
        month=datetime.datetime.now().month
        year=datetime.datetime.now().year
        expenditures=Expenditure.objects.filter(month=month,year=year)
        total=0
        for expenditure in expenditures:
            total+=expenditure.money
        return render(request,'expenditure.html',{'total':total,'year':year,
            'month':month,'expenditures':expenditures})


def expenditure_add(request):
    if request.method =='POST':
        try:
            name=request.POST.get('name')
            money=request.POST.get('money')
            year=request.POST.get('year')
            month=request.POST.get('month')
            remarks=request.POST.get('remarks')
            expenditure=Expenditure.objects.create(name=name,money=money,year=year,month=month,remarks=remarks)
            expenditure.save()
            return redirect('expenditure')
        except:
            year_choices=[y for y in range(2020,datetime.date.today().year+1)]
            month_choices=[m for m in range(1,13)]
            date_month=datetime.datetime.now().month
            date_year=datetime.datetime.now().year
            messages_1='*为必填内容！'
            return render(request,'expenditure_add.html',{'year_choices':year_choices,
            'month_choices':month_choices,'date_month':date_month,'date_year':date_year,'messages_1':messages_1})           
    else:
        year_choices=[y for y in range(2020,datetime.date.today().year+1)]
        month_choices=[m for m in range(1,13)]
        date_month=datetime.datetime.now().month
        date_year=datetime.datetime.now().year
        return render(request,'expenditure_add.html',{'year_choices':year_choices,
        'month_choices':month_choices,'date_month':date_month,'date_year':date_year})


def expenditure_example(request,expenditure_id):
    if request.method=='POST':
        try:
            expenditure=get_object_or_404(Expenditure, pk=expenditure_id)           
            name=request.POST.get('name')
            money=request.POST.get('money')
            year=request.POST.get('year')
            month=request.POST.get('month')
            remarks=request.POST.get('remarks')
            if name!='' and money!='' and remarks!='':
                expenditure.delete()
                expenditure=Expenditure.objects.create(name=name,money=money,year=year,
                month=month,remarks=remarks)
                expenditure.save()
                return redirect('expenditure')
            else:
                expenditure=get_object_or_404(Expenditure, pk=expenditure_id)
                messages_1='*为必填内容！'
                year_choices=[y for y in range(2020,datetime.date.today().year+1)]
                month_choices=[m for m in range(1,13)]
                return render(request,'expenditure_example.html',{'year_choices':year_choices,
                'month_choices':month_choices,'expenditure':expenditure,'messages_1':messages_1})
        except:
            expenditure=get_object_or_404(Expenditure, pk=expenditure_id)
            messages_1='*为必填内容！'
            year_choices=[y for y in range(2020,datetime.date.today().year+1)]
            month_choices=[m for m in range(1,13)]
            return render(request,'expenditure_example.html',{'year_choices':year_choices,
        'month_choices':month_choices,'expenditure':expenditure,'messages_1':messages_1})
    else:
        expenditure=get_object_or_404(Expenditure, pk=expenditure_id)
        year_choices=[y for y in range(2020,datetime.date.today().year+1)]
        month_choices=[m for m in range(1,13)]
        return render(request,'expenditure_example.html',{'year_choices':year_choices,
        'month_choices':month_choices,'expenditure':expenditure})
    
def income(request):
    if request.method =='POST':
        if  'search' in request.POST:
            month=request.POST.get('month')
            year=request.POST.get('year')
            error_msg= ''
            if not month:
               error_msg='请输入关键词'
               return render(request,'income.html',{'error_msg':error_msg})
            incomes=Income.objects.filter(month=month,year=year)
            total=0
            for income in incomes:
                total+=income.money
            return render(request,'income.html',{'total':total,'year':year,
            'month':month,'incomes':incomes})
        if 'add' in request.POST:
            return redirect('income_add')
    else:
        month=datetime.datetime.now().month
        year=datetime.datetime.now().year
        incomes=Income.objects.filter(month=month,year=year)
        total=0
        for income in incomes:
            total+=income.money
        return render(request,'income.html',{'total':total,'year':year,
        'month':month,'incomes':incomes})

def income_add(request):
    pass
    if request.method =='POST':
        try:
            name=request.POST.get('name')
            money=request.POST.get('money')
            year=request.POST.get('year')
            month=request.POST.get('month')
            follow=request.POST.get('follow')
            attribute=request.POST.get('attribute')
            remarks=request.POST.get('remarks')
            income=Income.objects.create(name=name,money=money,year=year,
            month=month,follow=follow,attribute=attribute,remarks=remarks)
            income.save()
            return redirect('income')
        except:
            follow_up=['王雨晴','胡雅丽','谢立虎','刘玲','米如','李兰']
            attribute_choice=['新生','续费']
            year_choices=[y for y in range(2020,datetime.date.today().year+1)]
            month_choices=[m for m in range(1,13)]
            date_month=datetime.datetime.now().month
            date_year=datetime.datetime.now().year
            messages_1='*为必填内容！'
            return render(request,'income_add.html',{'year_choices':year_choices,
            'follow_up':follow_up,'attribute_choice':attribute_choice,'month_choices':month_choices,'messages_1':messages_1,'date_month':date_month,'date_year':date_year})          
    else:
        follow_up=['王雨晴','胡雅丽','谢立虎','刘玲','米如','李兰']
        attribute_choice=['新生','续费']
        year_choices=[y for y in range(2020,datetime.date.today().year+1)]
        month_choices=[m for m in range(1,13)]
        date_month=datetime.datetime.now().month
        date_year=datetime.datetime.now().year
        return render(request,'income_add.html',{'year_choices':year_choices,
        'follow_up':follow_up,'attribute_choice':attribute_choice,'month_choices':month_choices,'date_month':date_month,'date_year':date_year})

def income_example(request,income_id):
    if request.method=='POST':
        try:
            income=get_object_or_404(Income, pk=income_id)           
            name=request.POST.get('name')
            money=request.POST.get('money')
            year=request.POST.get('year')
            month=request.POST.get('month')
            follow=request.POST.get('follow')
            attribute=request.POST.get('attribute')
            remarks=request.POST.get('remarks')
            if name!='' and money!='' and remarks!='':
                income.delete()
                income=Income.objects.create(name=name,money=money,year=year,
                month=month,follow=follow,attribute=attribute,remarks=remarks)
                income.save()
                return redirect('income')
            else:
                income=get_object_or_404(Income, pk=income_id)
                messages_1='*为必填内容！'
                year_choices=[y for y in range(2020,datetime.date.today().year+1)]
                month_choices=[m for m in range(1,13)]
                follow_up=['王雨晴','胡雅丽','谢立虎','刘玲','米如','李兰']
                attribute_choice=['新生','续费']
                return render(request,'income_example.html',{'year_choices':year_choices,
                'month_choices':month_choices,'follow_up':follow_up,'attribute_choice':attribute_choice,'income':income,'messages_1':messages_1})
        except:
            income=get_object_or_404(Income, pk=income_id)
            messages_1='*为必填内容！'
            year_choices=[y for y in range(2020,datetime.date.today().year+1)]
            month_choices=[m for m in range(1,13)]
            follow_up=['王雨晴','胡雅丽','谢立虎','刘玲','米如','李兰']
            attribute_choice=['新生','续费']
            return render(request,'income_example.html',{'year_choices':year_choices,
            'month_choices':month_choices,'follow_up':follow_up,'attribute_choice':attribute_choice,'income':income,'messages_1':messages_1})
    else:
        income=get_object_or_404(Income, pk=income_id)
        year_choices=[y for y in range(2020,datetime.date.today().year+1)]
        month_choices=[m for m in range(1,13)]
        follow_up=['王雨晴','胡雅丽','谢立虎','刘玲','米如','李兰']
        attribute_choice=['新生','续费']
        return render(request,'income_example.html',{'year_choices':year_choices,
        'month_choices':month_choices,'follow_up':follow_up,'attribute_choice':attribute_choice,'income':income})