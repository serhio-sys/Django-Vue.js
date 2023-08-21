from rest_framework import serializers
from .models import Post
from userapp.serializers import CustomUserSerializer

class PostSerializer(serializers.ModelSerializer):
    liked = CustomUserSerializer(read_only=True,many=True)

    class Meta:
        model = Post
        fields = ("created","name","desc","likes","liked","author")