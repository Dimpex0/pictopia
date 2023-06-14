from django.urls import path

from pictopia.account.views import ClientRegisterView, ClientLoginView

urlpatterns = [
    path('register/', ClientRegisterView.as_view(), name='client register page'),
    path('login/', ClientLoginView.as_view(), name='client login page')
]