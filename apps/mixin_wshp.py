# -*- coding: utf-8 -*-
"""
# @Time       : 2017/8/9 10:36
# @Author     : bangq
# @email      : my@yubangqi.com
# @File       : mixin_wshp.py
# @Description:
"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
