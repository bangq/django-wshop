from django.db import models
from datetime import datetime


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=500, verbose_name='分类名称')
    sort = models.IntegerField(default=0, verbose_name='排序值')
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = (
                         (0, '下架'),
                         (1, '上架'),
                     ),
    category = models.ForeignKey(Category, verbose_name='分类', null=True, blank=True)
    name = models.CharField(max_length=500, verbose_name='产品名称')
    unit = models.CharField(max_length=100, verbose_name='单位')
    keywords = models.CharField(max_length=200, verbose_name='关键词')
    image = models.ImageField(upload_to='product/%Y/%m', verbose_name='产品图片')
    barcode = models.CharField(max_length=100, verbose_name='条码')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='售价')
    market_price = models.DecimalField(max_length=8, decimal_places=2, verbose_name='市场价')
    cost_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='成本价')
    count = models.IntegerField(default=0, verbose_name='库存')
    sales_count = models.IntegerField(default=0, verbose_name='售出数量')
    is_show_sales_count = models.BooleanField(default=False, verbose_name='显示销量')
    has_invoice = models.BooleanField(default=False, verbose_name='提供发票')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name='状态')
    no_search = models.BooleanField(default=False, verbose_name='搜索是否显示')
    cannot_refund = models.BooleanField(default=False, verbose_name='支持退换货')
    order_value = models.IntegerField(default=0, verbose_name='排序值')
    details = models.TextField(verbose_name='详情')
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
