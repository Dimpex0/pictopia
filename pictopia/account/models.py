from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from pictopia.account.managers import ClientManager
from pictopia.account.validators import username_validation, name_validation


class Client(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )

    USERNAME_FIELD = 'email'

    objects = ClientManager()


class Profile(models.Model):
    username = models.CharField(
        max_length=30,
        unique=True,
        null=True,
        blank=True,
        validators=[
            username_validation
        ]
    )
    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        validators=[
            name_validation
        ]
    )
    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        validators=[
            name_validation
        ]
    )
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    image = models.ImageField(
        upload_to='profiles',
        null=True,
        blank=True,
    )
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    client = models.OneToOneField(
        Client,
        on_delete=models.CASCADE,
        unique=True,
        null=False,
        blank=False
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name and not self.last_name:
            return self.first_name
        elif self.last_name and not self.first_name:
            return self.last_name
        else:
            return None

    def __str__(self):
        return self.email
