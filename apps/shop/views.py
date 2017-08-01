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
        categorys = Category.objects.all().filter(is_abort=False, is_root=True).order_by('sort')

        return render(request, 'index.html', {
            'all_advs': all_advs,
            'root_categorys': categorys,
        })


class ListView(View):
    def get(self, request):
        category_id = request.GET.get('cid')
        goods_list = Goods.objects.all().filter(is_abort=False)
        category_label = '全部商品'
        if category_id:
            # goods_list = goods_list.filter(category_id == category_id)
            category = Category.objects.get(pk=category_id)
            if not category:
                category_label = category.name + '的商品'

        return render(request, 'list.html', {
            "category_label": category_label,
            "goods_list": goods_list,
        })
