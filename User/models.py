from django.db import models
from Tag.models import Tag
# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=120)
    contact = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank= True)
    photo = models.ImageField(null= True, blank=True)
    followed = models.ManyToManyField(Tag, related_name="wisher")


    def __str__(self) -> str:
        return self.name
    
    # @property
    # def rating(self):
    #     pass