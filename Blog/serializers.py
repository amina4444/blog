from rest_framework import serializers
from .models import Post, Comment
from rest_framework.exceptions import ValidationError

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'id author title'.split()

class CommentListserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id author body'.split()

class PostValidatorSerializer(serializers.Serializer):
    title = serializers.CharField(required=True,min_length=1,max_length=200)
    body = serializers.CharField(required=False, default="No text")
    





