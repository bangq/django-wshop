from django.contrib import admin

from .models import Goods, Category


# Register your models here.

class GoodsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'cost_price', 'price', 'count']

    fields = ('category', 'name', 'image', 'details', 'barcode', 'cost_price', 'price', 'count')

    class Media:
        js = (
            'kindeditor/kindeditor-all.js',
            'kindeditor/lang/zh-CN.js',
            'kindeditor/goods-config.js',
        )
        css = {
            'all': ('kindeditor/themes/default/default.css', 'kindeditor/plugins/code/prettify.css')
        }


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    fields = ('name', 'sort')
    model_icon = "fa fa-bars"


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)
