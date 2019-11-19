from django.db import models
from django_mysql.models import ListCharField

# Create your models here.

from django.contrib.auth.models import User

class Tweet(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hashtag = ListCharField(
        base_field=CharField(max_length=20),
        size=10
    )
