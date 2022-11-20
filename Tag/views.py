from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Tag, UserTagFollowing
from User.models import UserProfile
from User.serializer import UserProfileSerializer
from .serializer import TagSerializer
from rest_framework import status

from rest_framework import generics

# Create your views here.
class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailAPIView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class FollowTagView(APIView):
    def put(self, request, username,):
        try:
            new_following = UserProfile.objects.get(username__username=username)
            tagname = Tag.objects.get(title = tagname)
            # add following to currect user
            if new_following in tagname.get_followers():
                following =UserTagFollowing.objects.get(
                        userProfile_id = new_following,
                        following_tag_id = tagname
                    )
                following.delete()
            else:
                following =UserTagFollowing(
                        userProfile_id = new_following,
                        following_tag_id = tagname
                    )
                following.save()
            return Response(
                    {
                        "following":tagname.title
                    },
                    status=status.HTTP_202_ACCEPTED
                )
        except Tag.DoesNotExist:
            return Response( {
                    "error": True,
                    "error_msg": "Tag not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetTagFollowers(APIView):
    def get(self,request, tagname):
        followers = Tag.objects.get(
                title = tagname
            ).get_followers()
        print(followers)
        serializer = UserProfileSerializer(followers, many=True)
        return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )