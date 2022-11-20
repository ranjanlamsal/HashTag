from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.files.storage import default_storage

from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    genders = (
        ("MALE", "male"),
        ("FEMALE", "female"),
        ("OTHER", "other"),
    )
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    username = models.OneToOneField(User, on_delete= models.CASCADE)
    gender = models.CharField(
            choices =  genders,
            max_length = 10,
            blank=True)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        id = self.id
        return f"{self.username.username}({id})"

    def get_username(self):
        return self.username.username

    def get_posts(self):
        return self.posts.all()
        


def edit_or_create_userProfile(sender, instance, **kwargs):
    user = UserProfile.objects.filter(username=instance)
    if user.exists():
        user = user.first()
        user.first_name = instance.first_name
        user.last_name = instance.last_name
        user.save()
    else:
        user = UserProfile.objects.create(username=instance,
            first_name=instance.first_name,
            last_name=instance.last_name
            )


post_save.connect(edit_or_create_userProfile, sender=User)


