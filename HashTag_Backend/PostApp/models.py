
from django.db import models
from Tag.models import Tag
from User.models import UserProfile
from django.utils.translation import gettext_lazy as _
# Create your models here.

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Post(models.Model):
    status = (
        ("VERIFIED", "verified"),
        ("UNVERIFIED", "unverified"),
    )
    # title = models.CharField(max_length=120)
    content = models.TextField(blank= True, null= True)
    posted_by = models.ForeignKey(UserProfile,on_delete = models.CASCADE, blank = False, related_name='posted_by')
    image = models.ImageField(_("image"), upload_to=upload_to, default= 'posts/default.jpg')
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE, related_name='taged_title')
    upvote_users = models.ManyToManyField(UserProfile, default=None, blank = True, related_name = "upvoted_post")
    downvote_users = models.ManyToManyField(UserProfile, default=None, blank = True, related_name = "downvoted_post")
    created_at = models.DateTimeField(auto_now=True, blank= True, null=True)
    status = models.CharField(
        max_length=10,
        choices=status,
        default= "UNVERIFIED",
    )

    def tag_name(self):
        return self.tag.title
    
    def posted_by_user(self):
        return self.posted_by.username
    
    def __str__(self) -> str:
        return self.content

    def no_of_upvotes(self):
        upvote = self.upvote_users.all().count()
        # print(f"{upvote=} {downvote=}")
        return (upvote)
    
    def no_of_downvotes(self):
        downvote = self.downvote_users.all().count()
        return (downvote)

    def get_tag(self):
        return self.tag
    
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commented_on')
    commentor_by = models.ForeignKey(UserProfile,on_delete = models.CASCADE, blank = False)
    comment = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True )
    
    def __str__(self):
        return f"comment({self.id}) by {self.commentor_by} in {self.post}"
    def commented_by_user(self):
        return self.commentor_by.username
    
    # def create(self, validated_data):
    #     comment = Comment.objects.create(
    #         post=validated_data.get('post'),
    #         content=validated_data.get('content')
    #     )
    #     return comment


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    replied_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reply = models.TextField()
    reply_time = models.DateTimeField(auto_now_add=True)