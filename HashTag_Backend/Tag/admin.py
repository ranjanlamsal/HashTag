from django.contrib import admin
from .models import Tag, UserTagFollowing

# Register your models here.
admin.site.register(Tag)
admin.site.register(UserTagFollowing)