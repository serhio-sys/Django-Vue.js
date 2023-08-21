from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import CustomUserSerializer,get_user_model

class UsersViewSet(ReadOnlyModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = get_user_model().objects.all()

    