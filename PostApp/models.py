from django.db import models
from Tag.models import Tag
from User.models import UserProfile
# Create your models here.

class Post(models.Model):
    # title = models.CharField(max_length=120)
    content = models.TextField(blank= True, null= True)
    posted_by = models.ForeignKey(UserProfile,on_delete = models.CASCADE, blank = False, related_name='posted_by')
    photo = models.ImageField(null = True, blank = True)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE, related_name='taged_title')
    upvote_users = models.ManyToManyField(UserProfile, default=None, blank = True, related_name = "upvoted_post")
    downvote_users = models.ManyToManyField(UserProfile, default=None, blank = True, related_name = "downvoted_post")
    created_at = models.DateTimeField(auto_now=True, blank= True, null=True)

    def __str__(self) -> str:
        return self.content

    def no_of_upvotes(self):
        upvote = self.upvote_users.all().count()
        downvote = self.downvote_users.all().count()
        # print(f"{upvote=} {downvote=}")
        return (upvote - downvote)