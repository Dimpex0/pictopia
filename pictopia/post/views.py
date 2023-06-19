from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from pictopia.account.models import Profile
from pictopia.like.models import Like
from pictopia.post.forms import CreatePostForm
from pictopia.post.models import Post


class HomePageView(views.ListView):
    template_name = 'home-page.html'
    model = Post
    ordering = '-created_at'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['likes'] = Like.objects.all()
        return context


class CreatePostView(LoginRequiredMixin, views.CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'post/create-post-page.html'
    success_url = reverse_lazy('home page')

    def get_form_kwargs(self):
        kwargs = super(CreatePostView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


def delete_post(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.profile.client == request.user:
        post.delete()

    return redirect('home page')
