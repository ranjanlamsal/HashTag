from django.db import models
from Tag.models import Tag
from User.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank= True, null= True)
    posted_by = models.OneToOneField(User,on_delete=models.CASCADE, related_name="posted_by")
    photo = models.ImageField(null = True, blank = True)
    tag = models.OneToOneField(Tag, on_delete = models.CASCADE)
    no_of_likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, default=None, blank = True, related_name = "liked_by")


    def __str__(self) -> str:
        return self.title