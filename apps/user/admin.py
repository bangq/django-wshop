from django.contrib import admin
from .models import UserProfile, UserAddress
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserAddress)
