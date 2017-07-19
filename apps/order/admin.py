from django.contrib import admin
from .models import OrderDetail, Order, Customer


# Register your models here.

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail


class OrderAdmin(admin.ModelAdmin):
    search_fields = ['name', 'mobile', 'address']
    list_display = ['name', 'total_price', 'mobile', 'address']

    inlines = [
        OrderDetailInline,
    ]

    # 测试的功能，正式发布会去掉
    def save_model(self, request, obj, form, change):
        total_money = 0.0
        total_num = request.POST.get('orderdetail_set-TOTAL_FORMS')
        i = 0
        while i < int(total_num):
            price = request.POST.get("orderdetail_set-" + str(i) + "-price")
            count = request.POST.get("orderdetail_set-" + str(i) + "-count")
            if count is not None and price is not None and price != '':
                total_money = total_money + (float(price) * int(count))

            i = i + 1

        obj.total_price = str(total_money)
        super(OrderAdmin, self).save_model(request, obj, form, change)


class OrderDetailAdmin(admin.ModelAdmin):
    search_fields = ['order']
    list_display = ['order', 'product', 'price', 'count']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Customer)
