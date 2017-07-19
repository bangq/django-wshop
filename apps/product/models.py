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
    category = models.ForeignKey(Category, verbose_name='分类', null=True, blank=True)
    name = models.CharField(max_length=500, verbose_name='产品名称')
    image = models.ImageField(upload_to='product/%Y/%m', verbose_name='产品图片')
    barcode = models.CharField(max_length=100, verbose_name='条码')
    cost_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='成本价')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='售价')
    count = models.IntegerField(default=0, verbose_name='库存')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
