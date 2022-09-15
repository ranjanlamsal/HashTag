from django.db import models
from Tag.models import Tag
from User.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank= True, null= True)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name="posts")
    photo = models.ImageField(null = True, blank = True)
    tag = models.ManyToManyField(Tag, blank = True)
    no_of_likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, default=None, blank = True)


    def __str__(self) -> str:
        return self.title