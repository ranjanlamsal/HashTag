from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response

from Tag.serializer import TagSerializer
from .models import  User
from .serializer import UserSerializer
from Tag.models import Tag
from django.http import Http404
from rest_framework import status

from . import serializer
# Create your views here.

class UserAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    def post(self, request, pk):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserInfoAPI(APIView):
    def get(self, request, pk):
        user = User.objects.get(id = pk)
        serializer = UserSerializer(user)
        print(serializer.data)
        return Response(serializer.data)
    
    def post(self, request, pk):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFollowedTagAPI(APIView):
    def get(self, request, pk):
        user = User.objects.get(id = pk)
        followed_tags = Tag.objects.filter(user = user)
        print(followed_tags)
        serializer = TagSerializer(followed_tags, many = True)
        return Response(serializer.data)