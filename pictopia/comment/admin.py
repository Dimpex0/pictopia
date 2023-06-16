from django.contrib import admin

from pictopia.comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'profile', 'created_at']
