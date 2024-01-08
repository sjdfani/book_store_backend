from django.contrib import admin
from .models import Book, SaveItem


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title", "author", "language", "price", "publish")
    list_filter = ("author", "language", "publish")
    list_editable = ("publish",)


class SaveItemAdmin(admin.ModelAdmin):
    list_display = ("user", "book")
    list_filter = ("user", "book")


admin.site.register(Book, BookAdmin)
admin.site.register(SaveItem, SaveItemAdmin)
