from django.contrib import admin

from pictopia.post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_display = ['profile', 'created_at']
