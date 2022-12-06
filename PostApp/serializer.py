from pyexpat import model
from xml.dom import ValidationErr
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from Tag.serializer import TagSerializer
from Tag.models import Tag
from User.models import User
from .models import Comment
from User.serializer import UserPublicProfileSerializer, UserSerializer


from .models import Post

class CommentSerializer(ModelSerializer):
    # commented_by = UserPublicProfileSerializer(read_only = True)
    comment = serializers.CharField(required=True)
    class Meta:
        model = Comment
        fields=("id", "comment", "comment_time", "commented_by")
        depth = 1

class PostSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField('get_upvote_count')
    downvote_count = serializers.SerializerMethodField('get_downvote_count')
    comments = CommentSerializer(read_only=True, many=True)
    # tag_info = serializers.SerializerMethodField('get_tag_info')

    def get_upvote_count(self, obj):
        # print(obj.no_of_upvotes())
        return obj.no_of_upvotes()

    def get_downvote_count(self, obj):
        # print(obj.no_of_downvotes())
        return obj.no_of_downvotes()

    # def get_tag_info(self,obj):
    #     serializer = TagSerializer(obj.get_tag())
    #     return serializer.data
    class Meta:
        model = Post
        fields = "__all__"
        depth = 1

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

