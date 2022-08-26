from re import T
from django.db import models
from Tag.models import Tag
# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(null=True, blank= True)
    password = models.CharField(max_length=128, null=True, blank=True)
    password2 = models.CharField(max_length=128, null=True, blank=True)
    # photo = models.ImageField(null= True, blank=True)
    # followed = models.ManyToManyField(Tag, related_name="followed", default=None)


    def __str__(self) -> str:
        return self.name
    
    # @property
    # def rating(self):
    #     pass