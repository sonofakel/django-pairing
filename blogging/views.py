from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    queryset = Post.objects.order_by('-created_date')
    template_name = 'blogging/list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
