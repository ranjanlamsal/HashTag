from pyexpat import model
from xml.dom import ValidationErr
from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from Tag.serializer import TagSerializer


from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Post
        fields = "__all__"

class PostCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset = Post.objects.all())]
    )
    content = serializers.CharField(
        required = True
    )
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )
    def create(self, validated_data):
        postTocreate = Post.objects.create(
            title = validated_data['title'],
            content = validated_data['content']
        )
        postTocreate.save()

        return postTocreate