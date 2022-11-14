from django.shortcuts import redirect, render
from .models import User
from django.http import Http404, HttpResponseBadRequest
from User.serializer import UserLoginSerializer, UserLogoutSerializer, UserCreateSerializer, Userserializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from rest_framework import status
from rest_framework import authentication, permissions
from .permissions import IsStaffEditorPermission


from . import serializer
class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]

    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

user_detail_view = UserDetailAPIView.as_view()

class UserListCreateAPIView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]

    permission_classes = [permissions.DjangoModelPermissions]
    

userlistcreateview = UserListCreateAPIView.as_view()

class UserUpdaeteDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    authentication_classes =[
    authentication.SessionAuthentication,
    authentication.TokenAuthentication,
    ]

    permission_classes = [permissions.DjangoModelPermissions]
user_update_destroy_view = UserUpdaeteDestroyAPIView.as_view()
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