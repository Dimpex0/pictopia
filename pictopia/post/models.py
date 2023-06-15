from django.db import models

from pictopia.account.models import Profile


class Post(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    image = models.ImageField(
        upload_to='posts',
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
