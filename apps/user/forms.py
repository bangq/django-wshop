# -*- coding: utf-8 -*-
"""
# @Time       : 2017/8/9 10:11
# @Author     : bangq
# @email      : my@yubangqi.com
# @File       : forms.py
# @Description:
"""

from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
