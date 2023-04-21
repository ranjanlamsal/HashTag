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
from User.serializer import UserSerializer


from .models import Post

class CommentSerializer(ModelSerializer):
    def __init__(self, instance=None,**kwargs):
        remove_fields = kwargs.pop('remove_fields',None)
        super(CommentSerializer,self).__init__(instance,**kwargs)

        if remove_fields:
            #for multiple fields in a list
            for field_name in remove_fields:
                self.fields.pop(field_name)
    # commented_by = UserPublicProfileSerializer(read_only = True)
    comment = serializers.CharField(required=True)
    class Meta:
        model = Comment
        fields= ['id','comment', 'commented_by_user','post', 'comment_time']

class PostSerializer(serializers.ModelSerializer):
    upvote_count = serializers.SerializerMethodField('get_upvote_count')
    downvote_count = serializers.SerializerMethodField('get_downvote_count')
    comments = CommentSerializer(read_only=True, many=True)
    # posted_by_user = serializers.SerializerMethodField('get_who_posted')
    # tag_info = serializers.SerializerMethodField('get_tag_info')

    # def get_who_posted(self, obj):
    #     return obj.who_posted()

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
        fields = ['id','content', 'posted_by_user', 'created_at','image','tag_name', 'upvote_count', 'downvote_count', 'comments']

# class PostCreateSerializer(serializers.ModelSerializer):
#     # posted_by = 
#     content = serializers.CharField(
#         required = True
    # tag = serializers.PrimaryKeyRelatedField(
    #     queryset = Tag.objects.all(),
    #     required = True,
    #     many = False
    # # )
    # class Meta:
    #     model = Post
    #     fields = ['content', 'image']

