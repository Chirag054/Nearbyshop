from django.contrib import admin
from .models import Shop
# Register your models here.

class ShopAdmin(admin.ModelAdmin):
    pass

admin.site.register(Shop,ShopAdmin)