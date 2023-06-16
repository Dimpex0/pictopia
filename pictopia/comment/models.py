from django.db import models

from pictopia.account.models import Profile
from pictopia.post.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
