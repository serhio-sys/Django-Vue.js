from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .serializers import PostSerializer,PostCreationSerializer,PostsFormCreation
from rest_framework.decorators import action
from .models import Post
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.utils import timezone
from django.core.paginator import Paginator
from django.urls import reverse_lazy

import datetime

class BasePostsMixin():
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostsReadOnlyViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           BasePostsMixin,
                           GenericViewSet):
    per_page = 8

    
    def list(self, request, *args, **kwargs):
        string = request.GET.get("string", None)
        date = request.GET.get("date", None)
        to_oldest = request.GET.get("to_oldest", None)

        data = Post.objects.all()
        if string is not None:
            data = data.filter(name__icontains = string)
        if date is not None:
            data = data.filter(created__contains=datetime.date(int(date.split("-")[0]),int(date.split("-")[1]),int(date.split("-")[2])))
        if to_oldest is not None:
            print(to_oldest)
            if to_oldest:    
                data = data.filter(created__lte = datetime.datetime.now(tz=timezone.utc))
            else:    
                data = data.filter(created__gte = datetime.datetime.now(tz=timezone.utc))


        page = int(self.request.GET.get('page', 1))
        pagination = Paginator(object_list=data, per_page=self.per_page)
        results = self.serializer_class(pagination.page(page), many=True).data

        previous = None
        next = None
        string = self.request.GET.get('string', '')

        if(page > 1):
            previous = reverse_lazy('posts') + f'?string={string}&date={date}&to_oldest={to_oldest}&page={page - 1}' 
        if(page < pagination.num_pages):
            next = reverse_lazy('posts') + f'?string={string}&date={date}&to_oldest={to_oldest}&page={page + 1}'

        return Response(
            {
                'results': results,
                'previous_page': previous,
                'next_page': next,
                'page': page, 
                'max_page': pagination.num_pages
            }, 
            status=status.HTTP_202_ACCEPTED
        )  
    pass

class PostsCreateAPIView(APIView):
    def post(self,request):
        print(request.data)
        serializer = PostsFormCreation(request.data,request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response({"Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)



class PostsViewSet(mixins.CreateModelMixin,
                   BasePostsMixin,
                   GenericViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True,methods=["post"])
    def like(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.user != post.author:
            if not post.liked.filter(pk = request.user.pk).exists():
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
    