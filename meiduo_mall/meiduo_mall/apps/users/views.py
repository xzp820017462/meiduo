
import re
#from django.contrib.auth.models import User
from django.contrib.auth import login
from  meiduo_mall.apps.users.models import User
from django import http
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from django.db import DatabaseError
from meiduo_mall.utils.response_code import RETCODE
# Create your views here.

class UsermeCountView(View):
    def get(self,request,username):
        """"""
        count = User.objects.filter(username=username).count()
        return http.JsonResponse({'code':RETCODE.ok,'errmsg':'OK','count':count})



class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        """实现用户注册业务逻辑"""
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        allow = request.POST.get('allow')
        print(password,username,password2,mobile,allow)
        if not all ([username,password,password2,mobile,allow]):
            return http.HttpResponseForbidden('asd')

        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$',username):
            return http.HttpResponseForbidden('pease input username')

        if  password != password2:
            return http.HttpResponseForbidden('password and password2 not correct')

        if not re.match(r'1[3-9]\d{9}$',mobile):
            return http.HttpResponseForbidden('please input correct mobile number')

        if allow != 'on':
            return http.HttpResponseForbidden('please agree')

        try:
            user = User.objects.create_user(username=username,password=password,mobile=mobile)
        except DatabaseError as e:
            return render(request,'register.html',{"register_errmsg":e})

        #return redirect('/')
        login(request,user)
        return redirect(reverse('contents:index'))
