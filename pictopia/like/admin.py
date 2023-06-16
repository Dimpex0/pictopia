from django.contrib import admin

from pictopia.like.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'profile', 'created_at']
