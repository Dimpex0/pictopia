from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views

from pictopia.account.models import Profile
from pictopia.post.forms import CreatePostForm
from pictopia.post.models import Post


class HomePageView(views.ListView):
    template_name = 'home-page.html'
    model = Post
    ordering = '-created_at'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(client=self.request.user)
            context['profile'] = profile
        return context


class CreatePostView(LoginRequiredMixin, views.CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'post/create-post-page.html'

    def get_form_kwargs(self):
        kwargs = super(CreatePostView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
