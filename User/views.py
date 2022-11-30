from django.shortcuts import get_object_or_404, redirect, render
from .models import UserProfile
from .serializer import UserSerializer, UserProfileSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from rest_framework import status
from rest_framework import authentication, permissions
from .permissions import IsStaffEditorPermission

from Tag.models import Tag, UserTagFollowing


from . import serializer


class UserRecordView(APIView):
    """ API View to create or get user info.
    a POST request allows to create a new user.
    """
    def post(self, request):
        """make post request with user info to register"""
        request.data["username"] = request.data["username"].lower()
        request.data["first_name"] = request.data["first_name"].title()
        request.data["last_name"] = request.data["last_name"].title()
        email = request.data["email"]
        user = User.objects.filter(email = email)
        if user:
            return Response(
                    {
                        "email": ["A user with that email already exists."]
                    }
                )
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            update_data = serializer.data
            update_data.update({"success":True})
            return Response(
                    update_data,
                    status=status.HTTP_201_CREATED,
                )
        return Response(
               {
                   "error":True,
                   "error_msg": serializer.error_messages,
               },
               status=status.HTTP_400_BAD_REQUEST
               )


class UserProfileInfoView(APIView):
    def get(self, request):
        user = get_object(request)
        user_email = request.user.email
        serializer = UserProfileSerializer(user).data
        print(request.user.username)
        return Response(serializer)

    def put(self, request):
        user = get_object(request)
        request.data._mutable = True
        request.data["first_name"] = request.data["first_name"].title()
        request.data["last_name"] = request.data["last_name"].title()
        request.data._mutable = False
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = get_object(request)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def get_object(request):
    try:
        user = request.user
        return get_object_or_404(UserProfile, username=user)
        #return Traveller.objects.get(username=user)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]

    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

user_detail_view = UserDetailAPIView.as_view()

class UserListAPIView(generics.ListAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     authentication.TokenAuthentication,
    # ]

    # permission_classes = [permissions.DjangoModelPermissions]
    

userlistview = UserListAPIView.as_view()


# class UserUpdaeteDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = Userserializer
    # authentication_classes =[
    # authentication.SessionAuthentication,
    # authentication.TokenAuthentication,
    # ]

    # permission_classes = [permissions.DjangoModelPermissions]
# user_update_destroy_view = UserUpdaeteDestroyAPIView.as_view()

# class Login(generics.GenericAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer_class = UserLoginSerializer(data=request.data)
#         if not serializer_class.is_valid(raise_exception=True):
#             return Response(serializer_class.data, status=status.HTTP_200_OK)
#         return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


# class Logout(generics.GenericAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserLogoutSerializer

#     def post(self, request, *args, **kwargs):
#         serializer_class = UserLogoutSerializer(data=request.data)
#         if serializer_class.is_valid(raise_exception=True):
#             return Response(serializer_class.data, status=status.HTTP_200_OK)
#         return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


# def index(request):
#     return redirect('/api/login')


# class UserFollowedTags(APIView):
#     def get(self,request, username):
#         tagsFollowed = UserTagFollowing.objects.get(
#                 userProfile_id.username.username == username
#             )
#         print(tagsFollowed)
#         serializer = UserProfileSerializer(tagsFollowed, many=True)
#         return Response(
#                 serializer.data,
#                 status = status.HTTP_200_OK
#             )
