from django.shortcuts import get_object_or_404, redirect, render
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


class PostsCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     authentication.TokenAuthentication,
    # ]

    # permission_classes = [permissions.DjangoModelPermissions]

    def perform_create(self, serializer):
        tag = serializer.validated_data.get('tag')
        posted_by_id = serializer.validated_data.get('posted_by')
        # posted_by = User.objects.all().filter(id = posted_by_id)

        content = serializer.validated_data.get('content')

        if Tag.objects.all().filter(title  =  tag):
            responsedata = {
                'tag': tag.title,
                'posted_by': posted_by_id.username,
                'content': content
            }
            print(responsedata)
            return Response(responsedata)
        
        

Post_create_view = PostsCreateAPIView.as_view()

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def list(self, serializer):
    #     obj = get_object_or_404(Post)
    #     data = PostSerializer(obj, many = False).data
    #     posted_by_id = data.get('posted_by')
    #     posted_by_obj : User.objects.all().filter(id = posted_by_id)
    #     tag_id =  serializer.data.get('tag'),
    #     dataresponse = {
    #         "content" : serializer.data.get('content'),
    #         'id' : serializer.data.get('id'),
    #         "posted_by" : posted_by_obj.username,
    #         "tag" : Tag.objects.all().filter(id = tag_id).title
    #     }
    #     return Response(dataresponse)


Post_list_view = PostListAPIView.as_view()

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
