from django.contrib.auth.models import User

from blogging.models import Post
from blogging.forms import PostForm
from django import forms

from django.shortcuts import render, redirect
from django.utils import timezone

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from rest_framework import permissions
from blogging.serializers import UserSerializer, PostSerializer, CategorySerializer

from blogging.models import Post, Category


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.published_date = timezone.now()
            new_post.save()
            return redirect("/")

    form = PostForm()
    return render(request, "blogging/add_post.html", {"form": form})


class PostListView(ListView):
    queryset = Post.objects.order_by("-created_date").exclude(
        published_date__exact=None
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed
    """

    queryset = Post.objects.all().order_by("-created_date")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categorys to be viewed
    """

    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
