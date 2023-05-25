# from uuid import uuid4
# from django.db.models import Q # for queries
# from django.contrib.auth.models import User
# from nbformat import ValidationError
# from rest_framework import serializers
# from rest_framework.validators import UniqueTogetherValidator
from .models import UserProfile

from Tag.models import Tag


# from rest_framework import serializers
# from .models import UserProfile
# from rest_framework import serializers
# from rest_framework.validators import UniqueTogetherValidator
# from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from PostApp.models import Post


class NewRegisterSerializer(RegisterSerializer):
    # first_name = serializers.CharField();
    # last_name = serializers.CharField();
    def custom_signup(self, request, user):
        # user.first_name = request.data['first_name']
        # user.last_name = request.data['last_name']
        user.save()

class NewLoginSerializer(LoginSerializer):
    # parser_classes = [MultiPartParser, FormParser, JSONParser]
    pass 

class UserDetailSerializer(UserDetailsSerializer):
    pass
# class UserSerializer(serializers.ModelSerializer):
#     permission_classes = [IsAuthenticated]
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
#     class Meta:
#         model = User
#         fields = (
#                 'id',
#                 'username',
#                 'first_name',
#                 'last_name',
#                 'email',
#                 'password',
#                 )
#         validators = [
#                 UniqueTogetherValidator(
#                     queryset=User.objects.all(),
#                     fields=['username', 'email']
#                     )
#                 ]


class UserProfileSerializer(serializers.ModelSerializer):
    tagcount = serializers.SerializerMethodField('get_tag_count', read_only=True)
    postcount = serializers.SerializerMethodField('get_post_count', read_only=True)

    def get_post_count(self, obj):
        return Post.objects.filter(posted_by = obj).count()

    def get_tag_count(self, obj):
        return Tag.objects.filter(created_by = obj).count()
    class Meta:
        model = UserProfile
        fields = ['username', 'id', 'first_name', 'last_name','email', 'tagcount', 'postcount']

# class UserPublicProfileSerializer(serializers.ModelSerializer):
#     username = serializers.SlugRelatedField(slug_field='username', read_only=True)
#     class Meta:
#         model = UserProfile
#         fields = ['username', 'id', 'first_name', 'last_name']
#         depth = 1




# class UserLoginSerializer(serializers.ModelSerializer):
#     # to accept either username or email
#     username = serializers.CharField()
#     password = serializers.CharField()
#     token = serializers.CharField(required=False, read_only=True)

#     def validate(self, data):
#         # user,email,password validator
#         username = data.get("username", None)
#         password = data.get("password", None)
#         if not username and not password:
#             raise ValidationError("Details not entered.")
#         user = None
#         # if the email has been passed
#         if '@' in username:
#             user = UserProfile.objects.filter(
#                 Q(email=username) &
#                 Q(password=password)
#                 ).distinct()
#             if not user.exists():
#                 raise ValidationError("User credentials are not correct.")
#             user = UserProfile.objects.get(email=username)
#         else:
#             user = UserProfile.objects.filter(
#                 Q(username=username) &
#                 Q(password=password)
#             ).distinct()
#             if not user.exists():
#                 raise ValidationError("User credentials are not correct.")
#             user = UserProfile.objects.get(username=username)
#         if user.ifLogged:
#             raise ValidationError("User already logged in.")
#         user.ifLogged = True
#         data['token'] = uuid4()
#         user.token = data['token']
#         user.save()
#         return data

#     class Meta:
#         model = UserProfile
#         fields = (
#             'username',
#             'token',
#             'password'
#         )

#         read_only_fields = (
#             'token',
#             'password'
#         )


# class UserLogoutSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(required =True)
#     status = serializers.CharField(required=False, read_only=True)

#     def validate(self, data):
#         username = data.get('username')
#         user = None
#         try:
#             user = UserProfile.objects.get(username=username)
#             if not user.ifLoogged:
#                 raise ValidationError("User is not logged in.")
#                 return
#         except Exception as e:
#             raise ValidationError(str(e))
#             return e
#         user.ifLogged = False
#         user.token = ""
#         user.save()
#         data['status'] = "User is logged out."
#         return data

#     class Meta:
#         model = UserProfile
#         fields = (
#             'username',
#             'status',
#         )
