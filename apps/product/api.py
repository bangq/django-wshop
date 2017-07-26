# -*- coding: utf-8 -*-
"""
# @Time       : 2017/7/25 16:56
# @Author     : bangq
# @email      : my@yubangqi.com
# @File       : api.py
# @Description:
"""
from .serializers import GoodsSerializer, CategorySerializer
from rest_framework import viewsets, permissions

from .models import Category, Goods


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permissions = (permissions.AllowAny,)


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permissions = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Goods.objects.all()
        goods_name = self.request.query_params.get('name', None)
        category_id = self.request.query_params.get('categoryId', None)
        if not goods_name:
            queryset = queryset.filter(name=goods_name)
        if not category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset
