from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=120, null = False)
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=255,null=False)
    password = models.CharField(max_length=32)
    password2 = models.CharField(max_length=32)
    ifLogged = models.BooleanField(default=False)

    # username = models.CharField(max_length=120, null=True, blank=True)
    # email = models.EmailField(null=True, blank= True)
    # password = models.CharField(max_length=128, null=True, blank=True)
    # password2 models.CharField(max_length=128, null=True, blank=True)
    # photo = models.ImageField(null= True, blank=True)
    # followed = models.ManyToManyField(Tag, related_name="followed", default=None)


    def __str__(self) -> str:
        return self.username
    
    # @property
    # def rating(self):
    #     pass
