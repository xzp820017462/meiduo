from django.shortcuts import render
from django.views import View

# Create your views here.
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        """实现用户注册业务逻辑"""
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('passowrd2')
        mobile = request.POST.get('mobile')
        allow = request.POST.get('allow')
