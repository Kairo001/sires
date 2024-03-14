from django.contrib import admin
from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_active", "is_staff", "date_joined", "last_login", "is_superuser")
    list_display_links = ("email",)
    search_fields = ("email",)
    list_filter = ("is_active", "is_superuser")


admin.site.register(User, UserAdmin)
