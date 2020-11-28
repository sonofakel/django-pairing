from django.urls import path, include
from rest_framework import routers
from blogging import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"posts", views.PostViewSet)
router.register(r"categories", views.CategoryViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", views.PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="blog_detail"),
]
