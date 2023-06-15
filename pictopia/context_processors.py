from pictopia.account.models import Profile


def current_profile(request):
    if request.user.is_authenticated:
        return {'current_profile': Profile.objects.get(client=request.user)}
    else:
        return {'current_profile': None}
