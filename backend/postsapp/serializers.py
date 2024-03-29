from rest_framework import serializers
from .models import Post
 

class PostSerializer(serializers.ModelSerializer):
    liked = serializers.StringRelatedField(read_only=True,many=True)

    class Meta:
        model = Post
        fields = ('id',"created","name","desc",'image',"likes","liked","author")
    
class PostCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('__all__')
 