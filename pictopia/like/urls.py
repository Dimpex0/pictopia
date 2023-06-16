from django.urls import path

from pictopia.like.views import like_post

urlpatterns = [
    path('<post_pk>/', like_post, name='like/dislike post')
]
