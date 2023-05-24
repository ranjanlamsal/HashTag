# from uuid import uuid4
# from django.db.models import Q # for queries
# from django.contrib.auth.models import User
# from nbformat import ValidationError
# from rest_framework import serializers
# from rest_framework.validators import UniqueTogetherValidator
# from .models import UserProfile

# from Tag.models import Tag


# from rest_framework import serializers
# from .models import UserProfile
# from rest_framework import serializers
# from rest_framework.validators import UniqueTogetherValidator
# from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


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
