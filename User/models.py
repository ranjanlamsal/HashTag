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

    def __str__(self) -> str:
        return self.username
    
    # @property
    # def rating(self):
    #     pass
