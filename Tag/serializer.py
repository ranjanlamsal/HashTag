from rest_framework import serializers

from .models import Tag
from User.models import UserProfile
from PostApp.models import Post

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
        fields = "__all__"
        depth = 1


class TagCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=120,
        required=True)
    content = serializers.CharField(
        required = True
    )
    class Meta:
        model = Tag
        fields = "__all__"
        depth = 1