from django.urls import path,re_path
from finance import views


urlpatterns = [
    path('finance/',views.finance,name='finance'),
    path('finance/expenditure/',views.expenditure,name='expenditure'),
    path('finance/expenditure_add/',views.expenditure_add,name='expenditure_add'),
    path('finance/expenditure_example/<int:expenditure_id>/',views.expenditure_example,name='expenditure_example'),
    path('finance/income/',views.income,name='income'),
    path('finance/income_add/',views.income_add,name='income_add'),
    path('finance/income_example/<int:income_id>/',views.income_example,name='income_example')
]