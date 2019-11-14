from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    topic = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    id = models.CharField(max_length=30, primary_key=True)
