from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.mixin_wshop import LoginRequiredMixin
from .forms import LoginForm



# 用户登录
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            # 上面的 authenticate 方法 return user
            user = authenticate(username=user_name, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponsePermanentRedirect(reverse('index'))
                return render(request, 'login.html', {'msg': '用户未激活！'})
            return render(request, 'login.html', {'msg': '用户名或者密码错误！'})

        return render(request, 'login.html', {'form_errors': login_form.errors})


# 用户登出
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponsePermanentRedirect(reverse('index'))


class UserIndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user-index.html')
