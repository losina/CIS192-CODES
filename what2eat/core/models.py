from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    id = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    url = models.URLField()
    address = models.TextField()



class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    restaurant = models.ManyToManyField(Restaurant)
    def __str__(self):
        return self.name


class CategoryList(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    
class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    restaurant =  models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    class Meta:
       unique_together = ("user", "category")