from django.shortcuts import redirect, render
from .models import Post
from django.http import Http404, HttpResponseBadRequest
from PostApp.serializer import PostCreateSerializer, PostSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics

from Tag.models import Tag
from User.models import User

from Tag.serializer import TagSerializer
from rest_framework import status
from rest_framework import authentication, permissions


# Create your views here.

class PostsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]

    permission_classes = [permissions.DjangoModelPermissions]
    
    def perform_create(self, serializer):
        tag = serializer.validated_data.get('tag')
        if tag in Tag.objects.all():
            serializer.save(tag= tag)
            return Response(serializer.data)
        return Response({"invalid": "tag doesnot exists"}, status = 404)
        
        

Post_list_create_view = PostsListCreateAPIView.as_view()

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]

    permission_classes = [permissions.DjangoModelPermissions]
    
Post_detail_view = PostDetailAPIView.as_view()

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]

    permission_classes = [permissions.DjangoModelPermissions]
    
Post_update_view = PostUpdateAPIView.as_view()

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]
Post_delete_view = PostDeleteAPIView.as_view()
