# -*- coding: utf-8 -*-
"""
# @Time       : 2017/7/25 17:30
# @Author     : bangq
# @email      : my@yubangqi.com
# @File       : serializers.py
# @Description:
"""

from rest_framework import serializers
from .models import Order, OrderDetail


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Mate:
        model = Order
        fields = ('id', 'user_id', 'order_no', 'total_price', 'name', 'mobile', 'address', 'create_time', 'status',
                  'remark')
