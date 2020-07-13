from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection
from meiduo_mall.libs.captcha.captcha import captcha
from django import http
from meiduo_mall.meiduo_mall.utils.response_code import RETCODE
import random
from meiduo_mall.meiduo_mall.apps.verifications.yuntongxun.sms import CCP

# Create your views here.
class ImageCodeView(View):

    def get(self,request,uuid):
        text, image = captcha.generate_captcha()

        redis_conn = get_redis_connection('verify_codes')
        redis_conn.setex('img_%s' % uuid,300,text)

        #return HttpResponse(image,content_type="image/jpg")
        return  http.HttpResponse(image,content_type='image/jpeg')

class SMSCodeView(View):
    def get(self,request,mobile):
         image_code_client = request.GET.get('image_code')
         uuid = request.GET.get('uuid')

         if not all([image_code_client,uuid]):
            return http.HttpResponseForbidden('less canshu')

         redis_conn = get_redis_connection('verify_code')
         image_code_server = redis_conn.get('img_%s' % uuid)
         if image_code_server is None:
           return http.JsonResponse({'code':RETCODE.IMAGECODEERR,'errmsg':'error image'})

         redis_conn.delete('img_%s' % uuid)
         image_code_server = image_code_server.decode()
         if image_code_client.lower() != image_code_server.lower():
             return http.JsonResponse({'code':RETCODE.IMAGECODEERR,'errmsg':'error mobile'})

         sms_code = '%06d'% random.randint(0,999999)
         redis_conn.setex('sms_%s' % mobile, 300, sms_code)

         CCP().send_template_sms(mobile,[sms_code,300//60],1)

         return http.JsonResponse({'code':RETCODE.OK,'errmsg':'None'})