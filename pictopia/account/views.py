from django.contrib.auth import get_user_model, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from pictopia.account.forms import ClientRegisterForm, ProfileEditForm
from pictopia.account.models import Profile
from pictopia.comment.models import Comment
from pictopia.like.models import Like
from pictopia.post.models import Post

UserModel = get_user_model()


def client_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('home page')


class ClientRegisterView(views.CreateView):
    model = UserModel
    template_name = 'account/register.html'
    form_class = ClientRegisterForm

    def get_success_url(self):
        return reverse_lazy('home page')


class ClientLoginView(auth_views.LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return self.get_redirect_url() or self.get_default_redirect_url()


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'account/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_profile = self.get_object()
        comments = Comment.objects.all()
        comments_count = 0
        for comment in comments:
            if comment.post.profile == current_profile:
                comments_count += 1

        likes = Like.objects.all()
        likes_count = 0
        for like in likes:
            if like.post.profile == current_profile:
                likes_count += 1

        context['profile'] = current_profile
        context['likes_count'] = likes_count
        context['comments_count'] = comments_count
        context['posts'] = Post.objects.filter(profile=self.get_object()).order_by('-created_at')
        return context

    def get_object(self, queryset=None):
        return Profile.objects.get(id=self.kwargs['profile_pk'])


class ProfileEditView(LoginRequiredMixin, views.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'account/edit.html'

    def get_success_url(self):
        return reverse('profile details page', kwargs={'profile_pk': self.get_object().pk})

    def get_object(self, queryset=None):
        return Profile.objects.get(client=self.request.user)
