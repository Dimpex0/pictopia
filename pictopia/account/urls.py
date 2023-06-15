from django.urls import path

from pictopia.account.views import ClientRegisterView, ClientLoginView, client_logout, ProfileDetailsView, \
    ProfileEditView

urlpatterns = [
    path('register/', ClientRegisterView.as_view(), name='client register page'),
    path('login/', ClientLoginView.as_view(), name='client login page'),
    path('logout/', client_logout, name='logout'),
    path('profile/<int:profile_pk>/', ProfileDetailsView.as_view(), name='profile details page'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile edit page'),
]
