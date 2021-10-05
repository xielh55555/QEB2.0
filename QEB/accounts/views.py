from django.contrib import auth
from django.shortcuts import redirect, render
from django import forms

# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['is_login']=True
            request.session['user_id'] = user.id
            request.session['user_name'] =user.username
            return redirect('home')
        else:
            return render(request,'signin.html')
    return render(request,'signin.html')


def log_out(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("home")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("home")


def register(request):
    pass






