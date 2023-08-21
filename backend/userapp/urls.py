from django.urls import path,re_path,include
from .views import UsersViewSet

urlpatterns = [
    path("",UsersViewSet.as_view({"get":"list"})),
    path("<pk>/", UsersViewSet.as_view({"get":"retrieve"})),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]