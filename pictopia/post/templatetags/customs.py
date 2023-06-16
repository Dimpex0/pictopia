from datetime import datetime

from django import template

from pictopia.account.models import Profile
from pictopia.comment.models import Comment
from pictopia.like.models import Like
from pictopia.post.models import Post

register = template.Library()


@register.filter(name='postedTime')
def postedTime(value: datetime):
    time = datetime.now()

    time_seconds = int(time.timestamp())
    value_seconds = int(value.timestamp())
    seconds_diff = time_seconds - value_seconds

    minutes = seconds_diff / 60
    hours = minutes / 60
    days = hours / 24
    months = days / 30.44
    years = months / 12

    if seconds_diff >= 0:
        if minutes >= 1:
            if hours >= 1:
                if days >= 1:
                    if months >= 1:
                        if years >= 1:
                            return str(int(years)) + ' years ago'
                        return str(int(months)) + ' months ago'
                    return str(int(days)) + ' days ago'
                return str(int(hours)) + ' hours ago'
            return str(int(minutes)) + ' minutes ago'
        return str(int(seconds_diff)) + ' seconds ago'


@register.simple_tag(name='postLiked')
def postLiked(post: Post, profile: Profile):
    likes = Like.objects.filter(post=post, profile=profile)
    if likes:
        return True
    return False


@register.simple_tag(name='postComments')
def postComments(post_pk):
    post = Post.objects.get(pk=post_pk)
    return Comment.objects.filter(post=post).order_by('-created_at')
