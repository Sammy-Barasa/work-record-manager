from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authentication.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'is_staff',
                    'is_verified', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
            }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
