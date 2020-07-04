from jinja2 import Environment
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage

def jinja2_enviroment(**options):
    """jinja2环境"""
    #创建环境
    env = Environment(**options)
    #返回环境对象
    env.globals.update({
        "static":staticfiles_storage.url, #获取静态文件的前缀
        "url":reverse, #反向解析
    })
    #自定义语法 ： static. {{static{'静态文件相对路径') }}

    #return 对象
    return env

