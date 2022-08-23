from rest_framework import serializers

from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    # my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Tag
        fields = "__all__"