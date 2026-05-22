from rest_framework import serializers
from .models import Post, Comment
from rest_framework.exceptions import ValidationError

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'id author title'.split()


class CommentListserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id author body created_at updated_at'.split()


class PostValidatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'title  body'.split()


class CommentValidatorSerializer(serializers.ModelSerializer):
    class Meta:
       model = Comment
       fields = 'post body'.split()





