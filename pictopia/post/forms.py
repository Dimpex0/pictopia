from django import forms

from pictopia.account.models import Profile
from pictopia.post.models import Post


class CreatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['profile'].queryset = Profile.objects.filter(client=self.request.user)
        self.initial['profile'] = self.fields['profile'].queryset.first()

    class Meta:
        model = Post
        fields = ['profile', 'image', 'description']

        widgets = {
            'profile': forms.HiddenInput,
        }
