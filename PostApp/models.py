from django.db import models
from Tag.models import Tag
from User.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank= True, null= True)
    posted_by = models.ManyToManyField(User, blank = False)

    photo = models.ImageField(null = True, blank = True)
    tag = models.ManyToManyField(Tag, blank=False)
    no_of_likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, default=None, blank = True, related_name = "liked_by")


    def __str__(self) -> str:
        return self.title