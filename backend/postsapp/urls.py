from django.urls import path
from .views import PostsReadOnlyViewSet,PostsViewSet,PostsCreateAPIView


urlpatterns = [
    path("", PostsReadOnlyViewSet.as_view({"get":"list"}),name="posts"),
    path("liked/",PostsReadOnlyViewSet.as_view({"get":"liked"}),name="liked"),
    path("create/", PostsCreateAPIView.as_view()),
    path("<pk>/", PostsReadOnlyViewSet.as_view({"get":"retrieve"})),
    path("like/<pk>/", PostsViewSet.as_view({"post":"like"})),
]