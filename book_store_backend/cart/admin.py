from django.contrib import admin
from .models import Cart, PurchaseItem


class PurchaseItemsAdmin(admin.ModelAdmin):
    list_display = ("user", "count", "created_at", "updated_at")


class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "updated_at")


admin.site.register(Cart, CartAdmin)
admin.site.register(PurchaseItem, PurchaseItemsAdmin)
