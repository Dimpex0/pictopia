from random import randint

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from pictopia.account.models import Profile

UserModel = get_user_model()


class ClientRegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
        field_classes = {'username': UsernameField}

    def save(self, commit=True):
        client = super().save(commit=commit)
        username = 'user' + str(randint(0, 10000000))
        while Profile.objects.filter(username=username).exists():
            username = 'user' + str(randint(0, 10000000))
        profile = Profile(
            username=username,
            client=client,
            email=client.email
        )
        if commit:
            profile.save()


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'description', 'image']
        widgets = {
            'description': forms.Textarea
        }
        labels = {
            'description': 'Bio',
            'image': 'Profile image'
        }
