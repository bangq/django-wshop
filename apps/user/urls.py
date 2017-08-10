# -*- coding: utf-8 -*-
"""
# @Time       : 2017/8/9 10:51
# @Author     : bangq
# @email      : my@yubangqi.com
# @File       : urls.py
# @Description:
"""
from django.conf.urls import url, include
from .views import UserIndexView

urlpatterns = [
    url(r'^index/$', UserIndexView.as_view(), name='user_index'),
]
