from django.shortcuts import redirect, render
from .models import Post
from django.http import Http404, HttpResponseBadRequest
from PostApp.serializer import PostCreateSerializer, PostSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from urllib import request

from rest_framework import generics

from Tag.models import Tag
from User.models import User

from Tag.serializer import TagSerializer
from rest_framework import status
# Create your views here.

class PostsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        posted_by = serializer.validated_data.get('posted_by')
        tag = serializer.validated_data.get('tag')
        serializer.save(title, content, posted_by, tag)

Post_list_create_view = PostsListCreateAPIView.as_view()

    # def get(self, request):
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(posts, many=True)
    #     print(serializer.data)
    #     return Response(serializer.data)
    # def post(self, request):
    #     serializer = PostCreateSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

Post_detail_view = PostDetailAPIView.as_view()

class ModifyPostAPI(APIView):
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            DeletePostApi.delete(self, request, pk)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeletePostApi(APIView):
    def delete(self, request, pk):
        post = Post.objects.get(id=pk)
        post.delete()
        return