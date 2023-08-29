from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = routers.DefaultRouter().urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('posts/', include("postsapp.urls")),
    path('users/',include("userapp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)