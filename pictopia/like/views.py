from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from pictopia.account.models import Profile
from pictopia.like.models import Like
from pictopia.post.models import Post


@login_required
def like_post(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    profile = Profile.objects.get(client=request.user)
    for like in Like.objects.filter(profile=profile, post=post):
        if like.profile == post.profile:
            like.delete()
            return redirect('home page')
    Like(profile=profile, post=post).save()
    return redirect('home page')
