from django.contrib import admin
from core.models import User


class CustomUserAdmin(admin.ModelAdmin):
    """
    Админ панель пользователя
    """
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name']


admin.site.register(User, CustomUserAdmin)
