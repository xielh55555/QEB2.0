from django.db import models
from django.db.models.fields import CharField, DateField
import datetime

# Create your models here.
class Expenditure(models.Model):      #TODO  支出费用
    year_choices=[(y,y) for y in range(2020,datetime.date.today().year+1)]
    month_choices=[(m,m) for m in range(1,13)]

    name=models.CharField(max_length=50)
    money=models.FloatField(max_length=50)
    # date=models.DateField()
    year=models.IntegerField(choices=year_choices,default=datetime.datetime.now().year)
    month=models.IntegerField(choices=month_choices,default=datetime.datetime.now().month)
    remarks=CharField(max_length=200)

    def __str__(self):
        return self.name


class Income(models.Model):

    year_choices=[(y,y) for y in range(2020,datetime.date.today().year+1)]
    month_choices=[(m,m) for m in range(1,13)]
    follow_up=[
        ('王雨晴','王雨晴'),
        ('胡雅丽','胡雅丽'),
        ('谢立虎','谢立虎'),
        ('刘玲','刘玲'),
        ('陈米如','米如'),
        ('李兰','李兰')
    ]
    attribute_choice=[
        ('新生','新生'),
        ('续费','续费')
    ]
    name=models.CharField(max_length=50)
    money=models.FloatField(max_length=50)
    # date=models.DateField()
    year=models.IntegerField(choices=year_choices,default=datetime.datetime.now().year)
    month=models.IntegerField(choices=month_choices,default=datetime.datetime.now().month)
    follow=models.CharField(max_length=50,choices=follow_up )
    attribute=models.CharField(max_length=50,choices=attribute_choice )
    remarks=CharField(max_length=200)

    def __str__(self):
        return self.name


# income
# Commission
# wages
# stock