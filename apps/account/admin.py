"""Account app admin settings."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from account import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """User model admin settings."""

    list_display = ('id', 'username', 'short_name', 'date_joined', 'is_active',
                    'is_staff', 'is_superuser',)
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups',)
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {
            'fields': ('username', 'first_name', 'patronymic', 'last_name', )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'),
            'classes': ('collapse', )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'),
        }),
    )
    ordering = ('-date_joined', 'id',)

    def short_name(self, obj):
        """Get user's short name."""
        return obj.get_short_name()

    short_name.short_description = _('Name')
