import json
import random
import csv
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseBadRequest, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Tag, UserTagFollowing
from User.models import UserProfile
# from User.serializer import UserProfileSerializer
from .serializer import TagSerializer, TagCreateSerializer
from rest_framework import status

from rest_framework import generics
from rest_framework.parsers import MultiPartParser

tag_file = './staticfiles/tags.csv'

class TagView(APIView):
    # parser_classes = [MultiPartParser]
    def post(self, request):
        user = UserProfile.objects.get(username = request.user)

        serializer = TagCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save(created_by = user)

            #adding tags into tags.csv
            with open(tag_file, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([serializer.data['title'], serializer.data['content']])
                print('done')

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

class TrendingTags(APIView):
    def get(self, request):
        tags = sorted(Tag.objects.all(), key=lambda i: i.get_follower_count(), reverse=True)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class SelfTagGetView(APIView):
    def get(self, request):
        user = UserProfile.objects.get(username = request.user)
        if(user in UserProfile.objects.all()):
            tags = Tag.objects.filter(created_by = user)
            serializer = TagSerializer(tags, many=True)
            return Response(serializer.data)
        return Response({
            "error": "invalid_user"
        })
class SelfTagView(APIView):
    # parser_classes = [MultiPartParser]
    def put(self, request, id):
        tag = Tag.objects.get(id= id)
        if not tag:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if tag.created_by == UserProfile.objects.get(username = request.user):
            serializer = TagCreateSerializer(tag, data=request.data)
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
        tag = Tag.objects.get(id = id)
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


class TagDetailAPIView(APIView):
    def get(self, request,id):
        user= UserProfile.objects.get(username = request.user)
        if(user):
            tag = Tag.objects.get(id = id)
            serializer = TagSerializer(tag)
            return Response(serializer.data)

        return Response({
            "error": "invalid_user"
        })
class GetTagFollowers(APIView):
    def get(self,request, tagname):
        followers = Tag.objects.get(
                title = tagname
            ).get_followers()
        # print(followers)
        # print(type(followers))
        return JsonResponse({"followers": followers})
        # serializer = UserPublicProfileSerializer(followers, many=True)
        # print(serializer.data)
        # return Response(
        #         serializer.data,
        #         status = status.HTTP_200_OK
        #     )



class FollowTagView(APIView):
    def post(self, request, title):
        user = UserProfile.objects.get(username = request.user)
        tag = Tag.objects.get(title =title)
        followers_entry = tag.followers.all()
        print(followers_entry)
        follower_list = list()
        for entry in followers_entry:
            if(user == entry.followerUser):
                entry.delete()
                return Response(
                    {
                    'unfollower user': user.username,
                    'tag': tag.title,
                    'status': 'unfollowed'
                    },
                    status = status.HTTP_201_CREATED,
                    )
            # tag.followers.userProfile_id.remove(user)
        
        new_entry = UserTagFollowing(followerUser= user, following_tag_id=tag)
        new_entry.save()
        return Response(
            {
                'follower user': user.username,
                'tag': tag.title,
                'status': 'followed'
            },
            status = status.HTTP_201_CREATED,
            )

def get_tag(id):
    try:
        tag = Tag.objects.get(id = id)
    except Tag.DoesNotExist:
        return False
    return tag

def get_user(user):
    try:
        user = UserProfile.objects.get(username = user)
    except UserProfile.DoesNotExist:
        return None
    return user


class SuggestedTags(APIView):
    def get(self, request):
        user = UserProfile.objects.get(username=request.user)
        if(user in UserProfile.objects.all()):
            tags = Tag.objects.all()
            suggestedtags = []
            for tag in tags:
                if user not in tag.get_followers():
                    suggestedtags.append(tag)
            # random_posts = random.sample(list(suggestedtags), k = 6)
            serializer = TagSerializer(suggestedtags, many = True)
            return Response(serializer.data)
        return Response({
            "error":"invalid_user"
        })

class TagUserFollowSignal(APIView):
    def get(self, request, id):
        user = UserProfile.objects.get(username = request.user)
        tag = Tag.objects.get(id = id)
        if(user):
            if(user.username.username in tag.get_followers()):
                return Response({
                    "following": True
                })
            return Response({
                "following": False
            })
        return Response({
            "error": "invalid_user"
        })
