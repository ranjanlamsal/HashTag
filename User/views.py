import genericpath
from django.shortcuts import redirect, render
from .models import User
from django.http import Http404, HttpResponseBadRequest
from User.serializer import UserLoginSerializer, UserLogoutSerializer, UserCreateSerializer, Userserializer

from rest_framework.views import APIView
from rest_framework.response import Response
from urllib import request

from rest_framework import generics
from Tag.models import Tag
from Tag.serializer import TagSerializer
from rest_framework import status

from . import serializer
# Create your views here.

class UserAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = Userserializer(users, many=True)
        print(serializer.data)
        return Response(serializer.data)
    

    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     users = User.objects.all()
        # if serializer.initial_data == None:
        #     return {"message": "Required fields are missing"}

        # if users.filter(serializer.initial_data.filter('username')).exists():
        #     return {"message": "Username already exists"}
        # if not serializer.initial_data.keys('email').is_valid():
        #         return {"message": "Email not valid"}

        # if users.filter(serializer.initial_data.email).exists():
        #     return {"message": "Email already exists"}

        # if serializer.initial_data.get('username') in users.:
        #     return {"message": "Username already in use"}

        # if serializer.initial_data.keys('email') in users.keys('email'):
        #     return {"message": "email already in use"}

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserInfoAPI(APIView):
    def get(self, request, pk):
        user = User.objects.get(id = pk)
        serializer = Userserializer(user)
        print(serializer.data)
        return Response(serializer.data)
    
    def post(self, request, pk):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFollowedTagAPI(APIView):
    def get(self, request, pk):
        user1 = User.objects.get(id = pk)
        followed_tags = user1.followed
        print(followed_tags)
        serializer = TagSerializer(followed_tags, many = True)
        return Response(serializer.data)

class User_Create_APIView(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class Login(generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if not serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return redirect('/api/login')