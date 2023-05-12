from unittest.util import _MAX_LENGTH
from django.db import models
from User.models import UserProfile


class Tag(models.Model):
    #Info
    title = models.CharField(max_length=120, null = False, blank=False)
    content = models.TextField(blank= True, null= True)
    created_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name="created_by")
    created_at = models.DateTimeField(auto_now_add=True)

    #Rules 
    follow_to_post = models.BooleanField(default=False)
    follow_to_comment = models.BooleanField(default=False)
    follow_to_like = models.BooleanField(default=False)
    general_rules = models.TextField(blank=True, null=True)
    relevant_tags = models.TextField(blank=True, null=True)
    # followed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="followers")
    

    def __str__(self) -> str:
        return self.title

    def get_followers(self):
        follower = [x.followerUser.username for x in self.followers.all()]
        return follower

    def get_follower_count(self):
        return len(self.get_followers())
    
    def created_by_username(self):
        return self.created_by.username 
    
    def get_relevant_tags(self):
        relevant_tags = self.relevant_tags.lower()
        return relevant_tags.split(',')

    def get_tag_rules(self):
        return self.general_rules

        
# def get_following_tags(UserProfile):
#         following = [x.following_tag_id for x in UserProfile.following.all()]
#         return following

class UserTagFollowing(models.Model):
    """Buddha follows tag1
    user_id == buddha, following_tag_id = tag1

    TravellerFolowing instance
    
    id = 1,
    user_id = buddha,
    following_tag_id = tag1,

    id = 2,
    user_id = buddha,
    following_tag_id = tag2,

    id = 3,
    user_id = ranjan,
    following_tag_id = tag1,

    buddha = UserProfile.objects.get(username="buddha')
    ranjan  = UserProfile.objects.get(username="ranjan")
    buddha.following = id=1.following_tag_id, id=2.following_tag_id
    tag1.follower = id=1.UserProfile_id , id=3.UserProfile_id

    Traveller 
    following +
    followers +
    """

    followerUser = models.ForeignKey(
            UserProfile,
            on_delete=models.CASCADE,
            related_name="following"
        )
    following_tag_id = models.ForeignKey(
            Tag,
            on_delete=models.CASCADE,
            related_name="followers"
        )
    class Meta:
        unique_together = ('followerUser', 'following_tag_id',)