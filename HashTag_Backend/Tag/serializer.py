from rest_framework import serializers

from .models import Tag
from User.models import UserProfile
from PostApp.models import Post
from rest_framework.validators import UniqueValidator

class TagSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField('get_follower_list')
    # followers = serializers.SlugRelatedField('username')
    follower_count = serializers.SerializerMethodField('follower_list_count')
    post_count = serializers.SerializerMethodField('get_post_count')

    def get_post_count(self, obj):
        posts = Post.objects.filter(tag = obj).all()
        return posts.count()


    def get_follower_list(self, obj):
        return obj.get_followers()
    
    def follower_list_count(self, obj):
        return obj.get_follower_count()

    class Meta:
        model = Tag
        fields = ['id', 'title', 'created_by_username', 'created_at', 'followers', 'follower_count', 'post_count']

    def save(self, **kwargs):
        self.validated_data['title'] = self.validated_data['title'].upper()
        return super(TagCreateSerializer, self).save(**kwargs)

class TagCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=120,
        required=True,
        validators = [UniqueValidator(queryset=Tag.objects.all())]
        )
    content = serializers.CharField(
        required = False
    )
    class Meta:
        model = Tag
        fields = ['title', 'content']
    
    def save(self, **kwargs):
        self.validated_data['title'] = self.validated_data['title'].upper()
        return super(TagCreateSerializer, self).save(**kwargs)