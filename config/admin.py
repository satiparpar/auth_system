from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_golden', 'is_silvern')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'is_golden', 'is_silvern')}),  # Include 'is_golden' here
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


# admin.site.register(CustomUser, CustomUserAdmin)
