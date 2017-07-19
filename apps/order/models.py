from django.db import models
from user.models import UserProfile
from product.models import Product
from  datetime import datetime


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')
    mobile = models.CharField(max_length=50, verbose_name='手机')

    class Meta:
        verbose_name = '客户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='客户', null=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='总价')
    name = models.CharField(max_length=50, verbose_name='收件人', null=True)
    mobile = models.CharField(max_length=50, verbose_name='手机')
    address = models.CharField(max_length=500, verbose_name='地址')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    remark = models.CharField(max_length=500, verbose_name='备注')
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + '的订单'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, verbose_name='所属订单')
    product = models.ForeignKey(Product, verbose_name='产品')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='售价')
    count = models.IntegerField(default=0, verbose_name='数量')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '订单详情'
