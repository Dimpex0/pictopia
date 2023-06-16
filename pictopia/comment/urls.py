from django.urls import path

from pictopia.comment.views import create_comment, delete_comment

urlpatterns = [
    path('create-comment/<int:post_pk>/', create_comment, name='create comment'),
    path('delete/<int:comment_pk>/', delete_comment, name='delete comment')
]
