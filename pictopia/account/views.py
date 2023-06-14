from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from pictopia.account.forms import ClientRegisterForm


UserModel = get_user_model()


class ClientRegisterView(views.CreateView):
    model = UserModel
    template_name = 'account/register.html'
    form_class = ClientRegisterForm


class ClientLoginView(auth_views.LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return self.get_redirect_url() or self.get_default_redirect_url()
