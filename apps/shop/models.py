from django.db import models


# Create your models here.

class Adv(models.Model):
    title = models.CharField(max_length=200, verbose_name='幻灯片标题')
    order_value = models.IntegerField(default=0, verbose_name='排序值')
    image = models.ImageField(upload_to='adv/%Y/%m', verbose_name='幻灯片图片')
    link = models.CharField(max_length=1000, verbose_name='幻灯片链接')
    status = models.IntegerField(choices=((0, '隐藏'), (1, '显示')))
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '幻灯片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Notice(models.Model):
    title = models.CharField(max_length=200, verbose_name='公告标题')
    order_value = models.IntegerField(default=0, verbose_name='排序值')
    image = models.ImageField(upload_to='notice/%Y/%m', verbose_name='公告图片', null=True, blank=True)
    link = models.CharField(max_length=1000, verbose_name='公告链接', null=True, blank=True)
    status = models.IntegerField(choices=((0, '隐藏'), (1, '显示')))
    detail = models.TextField(verbose_name='公告详情')
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
