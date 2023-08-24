from rest_framework import serializers
from .models import Post
from userapp.serializers import UsernameSerializer

class PostSerializer(serializers.ModelSerializer):
    liked = serializers.StringRelatedField(read_only=True,many=True)

    class Meta:
        model = Post
        fields = ('id',"created","name","desc",'image',"likes","liked","author")