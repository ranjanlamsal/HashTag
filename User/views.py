from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import UserProfile
from .serializer import UserSerializer, UserProfileSerializer
from django.contrib.auth.models import User
from PostApp.models import Post
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
        
        email = request.data["email"]
        username = request.data["username"]
        user = User.objects.filter(email = email)
        user1 = User.objects.filter(username = username)
        if request.data["username"] is None:
            return JsonResponse(
                    {
                        "error": "username Required.",
                        "status" : status.HTTP_204_NO_CONTENT
                    }
                    # status = status.HTTP_204_NO_CONTENT
            )
        if request.data["first_name"] is None:
            return JsonResponse(
                    {
                        "error": "First Name Required.",
                        "status" : status.HTTP_204_NO_CONTENT
                        
                    }
                    # status = status.HTTP_204_NO_CONTENT
            )
        if request.data["last_name"] is None:
            return JsonResponse(
                    {
                        "error": "Last Name Required.",
                        "status" : status.HTTP_204_NO_CONTENT
                    }
                    # status = status.HTTP_204_NO_CONTENT
            )
        if request.data["email"] is None:
            return JsonResponse(
                    {
                        "error": "email Required.",
                        "status" : status.HTTP_204_NO_CONTENT
                    }
                    # status = status.HTTP_204_NO_CONTENT
            )
        if user:
            return JsonResponse(
                    {
                        "error": "A user with that email already exists.",
                        "status" : status.HTTP_400_BAD_REQUEST
                    }
                    # status = status.HTTP_400_BAD_REQUEST
                )
        if user1:
            return JsonResponse({
                        "error": "A user with that username already exists.",
                        "status" : status.HTTP_400_BAD_REQUEST
                    }
                    # status = status.HTTP_400_BAD_REQUEST
                    )


        request.data["username"] = request.data["username"].lower()
        request.data["first_name"] = request.data["first_name"].title()
        request.data["last_name"] = request.data["last_name"].title()

        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            update_data = serializer.data
            update_data.update({"success":True})
            return Response(
                    update_data,
                    status=status.HTTP_201_CREATED,
                )
        return JsonResponse(
               {
                   "error":True,
                   "error_msg": "Bad Request",
                   "status" : status.HTTP_400_BAD_REQUEST
               }
               
               )


class UserProfileInfoView(APIView):
    def get(self, request):
        user =UserProfile.objects.get(username = request.user)
        if user in UserProfile.objects.all():
            user_email = request.user.email
            serializer = UserProfileSerializer(user).data
            return Response(serializer)
        return JsonResponse({
            "error": "Invalid User"
        })

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
            print(user.username)
            return get_object_or_404(UserProfile, username=user)
            print(user.username)
            #return Traveller.objects.get(username=user)
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
# class UserListAPIView(generics.ListAPIView):

#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     authentication.TokenAuthentication,
    # ]

    # permission_classes = [permissions.DjangoModelPermissions]
    



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
