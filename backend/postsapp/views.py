from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .serializers import PostSerializer,PostCreationSerializer
from rest_framework.decorators import action
from .models import Post
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.utils import timezone
from .utils.paginate_response import paginate_response,paginate_response_with_filters

import datetime

class BasePostsMixin(GenericViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostsReadOnlyViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           BasePostsMixin):
    per_page = 8

    @action(detail=False,methods=["get"],permission_classes=[IsAuthenticated,])
    def liked(self, request):
        data = Post.objects.filter(liked__in = [request.user.pk,])
        return paginate_response(request=request,serializer_class=self.serializer_class,
                          per_page=self.per_page,data=data)
    @action(detail=False,methods=['get'],permission_classes=[IsAuthenticated,])
    def my_posts(self, request):
        data = Post.objects.filter(author = request.user.pk)

        return paginate_response(request=request,serializer_class=self.serializer_class,
                          per_page=self.per_page,data=data)


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

        string = self.request.GET.get('string', '')
        return paginate_response_with_filters(request=request,serializer_class=self.serializer_class,
                data=data,per_page=self.per_page,
                filters={"string":string,"date":date,"to_oldest":to_oldest})

    

class PostsCreateAPIView(APIView):
    def post(self,request):
        serializer = PostCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)



class PostsViewSet(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   BasePostsMixin):
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
    