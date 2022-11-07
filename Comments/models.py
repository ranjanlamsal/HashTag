from unittest.util import _MAX_LENGTH
from django.db import models
from User.models import User
from PostApp.models import Post
# Create your models here.

class Comment(models.Model):
    content = models.TextField(max_length = 10000)
    commented_by = models.OneToOneField(User, on_delete=models.CASCADE)
    commented_on = models.OneToOneField(Post, on_delete = models.CASCADE)


    def __str__(self) -> str:
        return self.content