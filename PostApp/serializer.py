from pyexpat import model
from xml.dom import ValidationErr
from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from Tag.serializer import TagSerializer
from Tag.models import Tag
from User.models import User
from User.serializer import Userserializer


from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Post
        fields = "__all__"

class PostCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required = True
    )
    content = serializers.CharField(
        required = True
    )
    class Meta:
        model = Post
        fields = "__all__"