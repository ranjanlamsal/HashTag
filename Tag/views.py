import json
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseBadRequest, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Tag, UserTagFollowing
from User.models import UserProfile
from User.serializer import UserProfileSerializer, UserPublicProfileSerializer
from .serializer import TagSerializer, TagCreateSerializer
from rest_framework import status

from rest_framework import generics
from rest_framework.parsers import MultiPartParser


class TagView(APIView):
    # parser_classes = [MultiPartParser]
    def post(self, request):
        user = UserProfile.objects.get(username = self.request.user)

        serializer = TagCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save(created_by = user)
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

class SelfTagView(APIView):
    def get(self, request, id):
        user = UserProfile.objects.get(username = request.user)
        tags = Tag.objects.filter(created_by = user)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def put(self, request, id):
        tag = get_tag(id)
        if not tag:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if tag.created_by == UserProfile.objects.get(username = request.user):
            serializer = TagCreateSerializer(tag, data=request.data,)
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
        tag = get_tag(id)
        if not tag:
            return Response(
                    {
                        "error": True,
                        "error_msg": "Post not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        if tag.user == UserProfile.objects.get(username = request.user):
            tag.delete()
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
class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailAPIView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class GetTagFollowers(APIView):
    def get(self,request, tagname):
        followers = Tag.objects.get(
                title = tagname
            ).get_followers()
        print(followers)
        return JsonResponse({"followers": followers})
        # serializer = UserPublicProfileSerializer(followers, many=True)
        # print(serializer.data)
        # return Response(
        #         serializer.data,
        #         status = status.HTTP_200_OK
        #     )

def get_tag(id):
    try:
        tag = Tag.objects.get(id = id)
    except Tag.DoesNotExist:
        return False
    return tag


class FollowTagView(APIView):
    def post(self, request, id):
        user = UserProfile.objects.get(username = request.user)
        tag = Tag.objects.get(id = id)
        # print(tag.get_followers())
        
        if(user.username in tag.get_followers()):
            for entry in tag.followers.all():
                entry.remove()
            # tag.followers.userProfile_id.remove(user)
        else:
            UserTagFollowing.add(userProfile_id= user, following_tag_id=tag)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = TagSerializer(tag)
        return Response(serializer.data)
