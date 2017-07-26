# -*- coding: utf-8 -*-
"""
# @Time       : 2017/7/25 16:42
# @Author     : bangq
# @email      : my@yubangqi.com
# @File       : serializers.py
# @Description:
"""

from rest_framework import serializers
from .models import Goods, Category


class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ('id', 'category', 'name', 'unit', 'keywords', 'image', 'barcode', 'price', 'market_price', 'count',
                  'sales_count', 'is_show_sales_count', 'has_invoice', 'status', 'cannot_refund', 'view_count',
                  'details')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'sort', 'pid', 'image')
