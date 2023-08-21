from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

urlpatterns = routers.DefaultRouter().urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('posts/', include("postsapp.urls")),
    path('users/',include("userapp.urls")),
]
