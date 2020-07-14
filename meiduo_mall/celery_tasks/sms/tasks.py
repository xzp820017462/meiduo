import sys
sys.path.append('/home/xu/meiduo/meiduo_mall')
from .yuntongxun.sms import CCP
from celery_tasks.main import celery_app

@celery_app.task(name='send_sms_code')
def send_sms_code(mobile,sms_code):
    send_ret = CCP().send_templates_sms(mobile,[sms_code,300],1)
    return send_ret