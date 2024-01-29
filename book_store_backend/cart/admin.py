from django.contrib import admin
from .models import PurchaseItem


class PurchaseItemsAdmin(admin.ModelAdmin):
    list_display = ("user", "count", "created_at", "updated_at")


admin.site.register(PurchaseItem, PurchaseItemsAdmin)
