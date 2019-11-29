from django.db import models


# Create your models here.

from django.contrib.auth.models import User

class Tweet(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes= models.IntegerField(default=0)


class HashTag(models.Model):
  name = models.CharField(max_length=64, unique=True)
  tweet = models.ManyToManyField(Tweet)
  def __unicode__(self):
    return self.name
  def __str__(self):
    return self.name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
       unique_together = ("user", "tweet")