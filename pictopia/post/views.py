from django.views import generic as views

from pictopia.post.models import Post


class HomePageView(views.ListView):
    template_name = 'home-page.html'
    model = Post
