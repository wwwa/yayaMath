# coding: utf-8
"""
@author
@date
@content

"""

from django.urls import re_path

from . import views

app_name = "myaccount"
urlpatterns = [
    re_path(r'^auth/$', views.wechat_auth, name='wechat_auth'),
    re_path(r'^user/info/$', views.get_wechat_user_info, name='get_wechat_user_info'),
]