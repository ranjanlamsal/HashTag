from unittest.util import _MAX_LENGTH
from django.db import models
from User.models import User
# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=120, null = False, blank=False)
    content = models.TextField(blank= True, null= True)
    rules = models.TextField(blank = True, default="None Rules Applied", max_length=10000)
    cover_photo = models.ImageField(null = True, blank = True)
    created_by = models.OneToOneField(User,on_delete=models.CASCADE, related_name="created_by")
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.title