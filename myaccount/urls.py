# coding: utf-8
"""
@author
@date
@content

"""

from django.urls import re_path

from . import views

app_name = "wechat"
urlpatterns = [
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^profile/update/$', views.profile_update, name='profile_update'),
]
