from django.urls import path
from .views import PostsReadOnlyViewSet,PostsViewSet


urlpatterns = [
    path("",PostsReadOnlyViewSet.as_view({"get":"list"}),name="posts"),
    path("<pk>/",PostsReadOnlyViewSet.as_view({"get":"retrieve"})),
    path("like/<pk>/",PostsViewSet.as_view({"post":"like"})),
]