from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from product.models import Goods, Category
from shop.models import Adv


# Create your views here.

class IndexView(View):
    def get(self, request):
        all_advs = Adv.objects.all().filter(status=1).order_by('order_value')

        return render(request, 'index.html', {
            'all_advs': all_advs
        })
