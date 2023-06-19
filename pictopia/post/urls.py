from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pictopia.post.views import HomePageView, CreatePostView, delete_post

urlpatterns = [
    path('', HomePageView.as_view(), name='home page'),
    path('create/', CreatePostView.as_view(), name='create post page'),
    path('delete/<int:post_pk>', delete_post, name='delete post page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
