from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount

class UserAccountAdmin(UserAdmin):
    ordering = ['email']
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password',)}),  # Include necessary fields like 'email', 'password'
        ('Personal info', {'fields': ('first_name', 'last_name', 'client_code', 'profile_image', 'phone', 'location', 'dob', 'branch')}),  # Add other personal info fields
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'role','groups', 'user_permissions')}),  # Include permissions and roles
        # Remove 'date_joined' from the fieldsets
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','first_name', 'last_name', 'client_code', 'profile_image', 'phone','branch', 'location', 'dob','is_active', 'is_staff', 'is_superuser', 'role'),
        }),
    )

admin.site.register(UserAccount, UserAccountAdmin)
