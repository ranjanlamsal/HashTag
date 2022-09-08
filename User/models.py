from django.db import models
# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=120)
<<<<<<< HEAD
    username = models.CharField(max_length=120, null=False)
    email = models.EmailField(max_length=255,null=False)
    password = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)
    photo = models.ImageField(null= True, blank=True)
    ifLogged = models.BooleanField(default=False)
    # followed = models.OneToManyField(Tag, related_name="followed", default=None)
=======
    username = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=True, blank= True)
    password = models.CharField(max_length=128, null=True, blank=True)
    password2 = models.CharField(max_length=128, null=True, blank=True)
    # photo = models.ImageField(null= True, blank=True)
    # followed = models.ManyToManyField(Tag, related_name="followed", default=None)
>>>>>>> d576d0a3d4a6e5786d50e728cbef4b8896511d44


    def __str__(self) -> str:
        return self.username
    
    # @property
    # def rating(self):
    #     pass
