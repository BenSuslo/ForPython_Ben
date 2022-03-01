"""为应用程序users定义URL模式"""
from tempfile import template
from django.urls import re_path
# from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    # 登录页面
    # URL中的单词users让Django在users/urls.py中查找，而单词login让它将请求发送给Django默认视图login
    re_path(r'login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 注册页面
    re_path(r'^register/$', views.register, name='register'),
    # 注销
    re_path(r'^logout/$', views.logout_view, name='logout'),
]