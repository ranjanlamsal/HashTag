from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from django.http import Http404, HttpResponseBadRequest
from PostApp.serializer import PostCreateSerializer, PostSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics

from Tag.models import Tag
from User.models import UserProfile

from Tag.serializer import TagSerializer
from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework.parsers import MultiPartParser



class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]
    permission_classes = [permissions.DjangoModelPermissions]
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


class SelfPostListCreateView(APIView):
    parser_classes = [MultiPartParser]
    def post(self, request):
        user = UserProfile.objects.get(username = self.request.user)

        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save(posted_by = user)
            return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED,
                )
        return Response(
               {
                   "error":True,
                   "error_msg": serializer.error_messages,
               },
               status=status.HTTP_400_BAD_REQUEST
               )

    def get(self, request):
        user = UserProfile.objects.get(username = request.user)
        print(user)
        posts = Post.objects.filter(posted_by = user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class SelfPostUpdateView(APIView):
    def put(self, request, id):
        post = get_post(id)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if post.posted_by == UserProfile.objects.get(username = request.user):
            serializer = PostCreateSerializer(post, data=request.data,)
            request.data._mutable = True
        
            if serializer.is_valid(raise_exception = ValueError):
                serializer.save()
                return Response(serializer.data)
            return Response(
                   {
                       "error":True,
                       "error_msg": serializer.error_messages,
                   },
                   status=status.HTTP_400_BAD_REQUEST
                   )

        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, id):
        post = get_post(id)
        if not post:
            return Response(
                    {
                        "error": True,
                        "error_msg": "Post not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        if post.posted_by == UserProfile.objects.get(username = request.user):
            post.delete()
            return Response({"success":"post deleted"},
                    status = status.HTTP_200_OK
                )
        return Response(
                {
                    "error": True,
                    "error_msg": "Not your post"
                },
                status = status.HTTP_401_UNAUTHORIZED
            )

class PostView(APIView):
    parser_classes = [MultiPartParser]
    def post(self, request):
        user = UserProfile.objects.get(username = self.request.user)

        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save(posted_by = user)
            return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED,
                )
        return Response(
               {
                   "error":True,
                   "error_msg": serializer.error_messages,
               },
               status=status.HTTP_400_BAD_REQUEST
               )



def get_post(id):
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return False
    return post


class TagPosts(APIView):
    def get(self, request, id):
        tag = Tag.objects.get(id=id)
        posts = Post.objects.filter(tag = tag)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class UserLikedPosts(APIView):
    def get(self, request, id):
        user = UserProfile.objects.get(id = id)
        posts = Post.objects.filter(upvote_users = user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class UpvotePost(APIView):
    def post(self, request, id):
        user = UserProfile.objects.get(username = request.user)
        post = Post.objects.get(id = id)
        if(user in post.downvote_users.all()):
            post.downvote_users.remove(user)
        else:
            post.upvote_users.add(user)
        serializer = PostSerializer(post)
        return Response(serializer.data)

class DownvotePost(APIView):
    def post(self, request, id):
        user = UserProfile.objects.get(username = request.user)
        post = Post.objects.get(id = id)
        if(user in post.upvote_users.all()):
            post.upvote_users.remove(user)
        else:
            post.upvote_users.add(user)
        serializer = PostSerializer(post)
        return Response(serializer.data)

