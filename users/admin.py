from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Add any customizations for the admin interface
    list_display = ('first_name', 'last_name','username', 'email', 'bio', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
