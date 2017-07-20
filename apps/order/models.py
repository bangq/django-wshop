from django.db import models
from user.models import UserProfile
from product.models import Goods


class Order(models.Model):
    Order_STATUS_CHOICES = (
        (-1, '已关闭'),
        (0, '待付款'),
        (1, '待发货'),
        (2, '待收货'),
        (3, '已完成'),
    )

    user = models.ForeignKey(UserProfile, verbose_name='客户', null=True)
    order_no = models.CharField(max_length=30, verbose_name='订单号')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='总价')
    name = models.CharField(max_length=50, verbose_name='收件人', null=True)
    mobile = models.CharField(max_length=50, verbose_name='手机')
    address = models.CharField(max_length=500, verbose_name='地址')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    status = models.IntegerField(choices=Order_STATUS_CHOICES, verbose_name='订单状态')
    remark = models.CharField(max_length=500, verbose_name='备注')
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + '的订单'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, verbose_name='所属订单')
    goods = models.ForeignKey(Goods, verbose_name='产品')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='售价')
    count = models.IntegerField(default=0, verbose_name='数量')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '订单详情'


class PayRecord(models.Model):
    order = models.ForeignKey(Order, verbose_name='所属订单')
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    trade_no = models.CharField(max_length=100, verbose_name='交易号')
    subject = models.CharField(max_length=1000, verbose_name='交易主题')
    money = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='交易金额')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    pay_time = models.DateTimeField(auto_now_add=True, verbose_name='支付时间')
    is_pay = models.BooleanField(default=False, verbose_name='是否支付')
    pay_type = models.IntegerField(choices=((1, '微信支付'), (2, '支付宝支付'), (3, '余额支付')), verbose_name='支付方式')
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '支付记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject
