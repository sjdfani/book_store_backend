from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "email", "is_staff", "is_active", "is_superuser")
    list_filter = ("is_staff", "is_active", "is_superuser")
    fieldsets = (
        ('Personal Information', {
         "fields": ("email", "fullname", "profile", "password")}),
        ("Permissions", {"fields": (
            "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Date and Time", {
         "fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        ('Personal Information', {
            "classes": ("wide",),
            "fields": ("email", "fullname", "profile", "password1", "password2")}),
        ("Permissions", {"fields": (
            "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
