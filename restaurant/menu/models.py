from django.db import models

# Create your models here.
class Meal(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	vegan = models.BooleanField()
	price = models.DecimalField(max_digits=6, decimal_places=2)