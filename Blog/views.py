from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from .serializers import PostListSerializer,PostSerializer,PostValidatorSerializer,CommentListserializer,CommentValidatorSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from .permissions import IsOwner


class CustomPagination(PageNumberPagination):
    page_size = 5
    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

class PostsListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostValidatorSerializer
        return PostListSerializer

    def perform_create(self, serializer):
      serializer.save(author=self.request.user)
    

class PostAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'   
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

class CommentsListAPIView(ListCreateAPIView):
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentValidatorSerializer
        return CommentListserializer
    
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['id'])
    
    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['id'])
        serializer.save(author=self.request.user, post=post)
    




