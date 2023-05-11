from pyexpat import model
from xml.dom import ValidationErr
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from Tag.serializer import TagSerializer
from Tag.models import Tag
from User.models import UserProfile
from .models import Comment, Reply
# from User.serializers import UserSerializer


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
    commentor_by = serializers.ReadOnlyField(source = 'commentor_by.username')
    comment = serializers.CharField(required=True)
    class Meta:
        model = Comment
        fields= ['id','post', 'commentor_by','comment', 'comment_time']
    
    def get_replies(self, obj):
        replies_queryset = obj.replies.all()
        replies_serializer = ReplySerializer(replies_queryset, many=True)
        return replies_serializer.data


class ReplySerializer(ModelSerializer):
    # reply_to = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all())
    replied_by_user = serializers.ReadOnlyField(source='replied_by.username')
    reply = serializers.CharField(required=True)

    class Meta:
        model = Reply
        fields = ['id', 'reply', 'replied_by_user', 'reply_time']
# class CommentSerializer(ModelSerializer):
#     def __init__(self, instance=None,**kwargs):
#         remove_fields = kwargs.pop('remove_fields',None)
#         super(CommentSerializer,self).__init__(instance,**kwargs)

#         if remove_fields:
#             #for multiple fields in a list
#             for field_name in remove_fields:
#                 self.fields.pop(field_name)
#     # commented_by = UserPublicProfileSerializer(read_only = True)
#     comment = serializers.CharField(required=True)
#     class Meta:
#         model = Comment
#         fields= ['id','comment', 'commented_by_user','post', 'comment_time']
# class ReplySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reply
#         fields = ('id', 'content', 'timestamp', 'comment')
#         read_only_fields = ('id', 'timestamp')   
        
        
# class CommentSerializer(serializers.ModelSerializer):
#     # replies = ReplySerializer(many=True, read_only=True)

#     class Meta:
#         model = Comment
#         fields = ('id', 'commentor_name', 'comment_text','timestamp', 'post')
#         # read_only_fields = ('id', 'timestamp', 'post')
    
#     def create(self, validated_data):
#         post_id = self.context.get('view').kwargs.get('post_id')
#         post = Post.objects.get(pk=post_id)
#         comment = Comment.objects.create(post=post, **validated_data)
#         return comment

    # def create(self, validated_data):
    #     return Comment.objects.create(
    #         content=validated_data.get('content'),
    #         post=self.context['post'],
    #     )  
        
              
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

