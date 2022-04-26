from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    post = models.CharField(max_length=256, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)  # auto_now=True
    likes = models.IntegerField(default=0, blank=True, null=True, editable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "post": self.post,
            "timestamp": self.timestamp.strftime("%b %d %Y, %H:%M:%S"),
            "likes": self.likes
        }


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="likeduser")
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name="likedpost")


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")  # user's followings
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")  # user's followers
