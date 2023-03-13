from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.files.storage import default_storage
from rest_framework.response import Response


class UserProfile(models.Model):
    genders = (
        ("MALE", "male"),
        ("FEMALE", "female"),
        ("OTHER", "other"),
    )
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    username = models.OneToOneField(User, on_delete= models.CASCADE)
    email = models.EmailField(max_length=200, blank = False)
    gender = models.CharField(
            choices =  genders,
            max_length = 10,
            blank=True
            )
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        id = self.id
        return f"{self.username}({id})"

    def get_username(self):
        return self.username.username

    def get_posts(self):
        return self.posts.all()

    def get_hashtags(self):
        return self.tags.all()


    def get_email(self):
        return self.email

    def get_private_details(self):
        data = {
            "email": self.email,
            "password" : self.password,
            "gender" : self.gender,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "reg_date" : self.reg_date,
        }
        return Response(data)

    def get_public_details(self):
        data = {
            "username" : self.username,
            "posts" : self.get_posts,
            "hashtags": self.get_hashtags,
        }

    def __str__(self) -> str:
        return self.username.username

def edit_or_create_userProfile(sender, instance, **kwargs):
    user = UserProfile.objects.filter(username=instance)
    if user.exists():
        user = user.first()
        user.first_name = instance.first_name
        user.last_name = instance.last_name
        user.email = instance.email
        user.save()
    else:
        user = UserProfile.objects.create(username=instance,
            first_name=instance.first_name,
            last_name=instance.last_name
            )


post_save.connect(edit_or_create_userProfile, sender=User)


