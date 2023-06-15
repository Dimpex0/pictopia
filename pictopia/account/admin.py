from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from pictopia.account.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class ClientAdmin(UserAdmin):
    ordering = ['date_joined']
    readonly_fields = ['date_joined']
    list_filter = []
    list_display = ['email', 'is_staff', 'is_superuser']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username']
