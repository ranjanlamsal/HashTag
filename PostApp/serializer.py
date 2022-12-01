from pyexpat import model
from xml.dom import ValidationErr
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from Tag.serializer import TagSerializer
from Tag.models import Tag
from User.models import User
from User.serializer import UserPublicProfileSerializer, UserSerializer


from .models import Comment, Post

class CommentSerializer(ModelSerializer):
    # commented_by = UserPublicProfileSerializer(read_only = True)
    comment = serializers.CharField(required=True)
    class Meta:
        model = Comment
        fields=("id", "comment", "comment_time")

class PostSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField('get_upvote_count')
    comments = CommentSerializer(read_only=True, many=True)

    def get_upvote_count(self, obj):
        print(obj.no_of_upvotes())
        return obj.no_of_upvotes()
    class Meta:
        model = Post
        fields = "__all__"
        depth = 2

class PostCreateSerializer(serializers.ModelSerializer):
    # posted_by = 
    content = serializers.CharField(
        required = True
    )
    # tag = serializers.PrimaryKeyRelatedField(
    #     queryset = Tag.objects.all(),
    #     required = True,
    #     many = False
    # )
    class Meta:
        model = Post
        fields = ['content']

