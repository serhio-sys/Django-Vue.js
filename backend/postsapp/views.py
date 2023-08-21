from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .serializers import PostSerializer
from rest_framework.decorators import action
from .models import Post
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class BasePostsMixin():
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostsReadOnlyViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           BasePostsMixin,
                           GenericViewSet):
    
    pagination_class = LimitOffsetPagination
    pass

class PostsViewSet(mixins.CreateModelMixin,
                   BasePostsMixin,
                   GenericViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True,methods=["post"])
    def like(self, pk,request, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.user != post.author:
            if request.user not in post.liked:
                post.liked.add(request.user)
                post.likes += 1
            else:
                post.liked.remove(request.user)
                post.likes -= 1
            post.save()
            return Response({"success"},status=status.HTTP_200_OK)
        else:
            return Response({"author can not like his posts"},status=status.HTTP_400_BAD_REQUEST)
    
    
    pass
    