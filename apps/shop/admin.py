from django.contrib import admin
from .models import Adv, Notice


# Register your models here.

class AdvAdmin(admin.ModelAdmin):
    fields = ('title', 'order_value',  'status', 'detail')


admin.site.register(Adv)
admin.site.register(Notice, AdvAdmin)
