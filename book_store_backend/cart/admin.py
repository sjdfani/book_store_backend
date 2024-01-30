from django.contrib import admin
from .models import PurchaseItem


class PurchaseItemsAdmin(admin.ModelAdmin):
    list_display = ("user", "count", "status", "created_at", "updated_at")
    list_filter = ("status",)


admin.site.register(PurchaseItem, PurchaseItemsAdmin)
