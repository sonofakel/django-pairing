from blogging.models import Post
from blogging.forms import PostForm
from django import forms

from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.published_date = timezone.now()
            new_post.save()
            return redirect('/')

    form = PostForm()
    return render(request, "blogging/add_post.html", {'form': form})


class PostListView(ListView):
    queryset = Post.objects.order_by("-created_date").exclude(
        published_date__exact=None
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"
