from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# model for restuarant. Save features selected from yelp search result
class Restaurant(models.Model):
    id = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    url = models.URLField()
    address = models.TextField()
    def __str__(self):
        return self.name
    
# category, or hashtags, that can classify restaurants 
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    restaurant = models.ManyToManyField(Restaurant)
    def __str__(self):
        return self.name

# relationship between a category and a user
class CategoryList(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    
# relationship between a category, a user and a restuarant 
class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    restaurant =  models.ForeignKey(Restaurant, on_delete=models.CASCADE)

