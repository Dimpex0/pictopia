from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from pictopia.account.models import Profile
from pictopia.comment.models import Comment
from pictopia.post.models import Post


@login_required
def create_comment(request, post_pk):
    profile = Profile.objects.get(client=request.user)
    post = Post.objects.get(pk=post_pk)
    Comment(profile=profile, post=post, text=request.POST['comment']).save()
    return redirect('home page')


@login_required
def delete_comment(request, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()
    return redirect('home page')
