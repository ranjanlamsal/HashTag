from pyexpat import model
from xml.dom import ValidationErr
from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from Tag.serializer import TagSerializer
from Tag.models import Tag
from User.models import User
from User.serializer import UserSerializer


from .models import Post

class PostSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField('get_upvote_count')

    def get_upvote_count(self, obj):
        print(obj.no_of_upvotes())
        return obj.no_of_upvotes()
    class Meta:
        model = Post
        fields = "__all__"
        depth = 1

class PostCreateSerializer(serializers.ModelSerializer):
    # posted_by = 
    content = serializers.CharField(
        required = True
    )
    tag = serializers.PrimaryKeyRelatedField(
        queryset = Tag.objects.all(),
        required = True,
        many = False
    )
    class Meta:
        model = Post
        fields = "__all__"
        depth = 1