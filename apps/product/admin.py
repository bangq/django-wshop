from django.contrib import admin

from .models import Goods, Category


# Register your models here.


class GoodsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['category', 'name', 'cost_price', 'price', 'count', 'status']
    list_display_links = ('name',)
    list_filter = ('category', 'status', 'is_abort',)
    fields = ('category', 'name', 'keywords', 'image', 'details', ('count', 'sales_count'),
              ('market_price', 'cost_price', 'price'),
              ('is_show_sales_count', 'has_invoice', 'cannot_refund', 'no_search'), 'status')

    actions = ['make_on_sale', 'make_off_sale', 'delete_selected']

    def make_on_sale(self, request, queryset):
        rows_updated = queryset.update(status=1)
        self.message_user(request, "上架了 %s 条商品." % rows_updated)

    make_on_sale.short_description = "上架选中的商品"

    def make_off_sale(self, request, queryset):
        rows_updated = queryset.update(status=0)
        self.message_user(request, "下架了 %s 条商品" % rows_updated)

    make_off_sale.short_description = "下架选中的商品"

    def delete_selected(self, request, queryset):
        queryset.update(is_abort=True)

    delete_selected.short_description = '删除所选项'

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
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        queryset.update(is_abort=True)

    delete_selected.short_description = '删除所选项'

    #   重写queryset 自定义筛选
    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        return qs.filter(is_abort=False)


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)
