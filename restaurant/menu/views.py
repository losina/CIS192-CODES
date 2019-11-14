from __future__ import unicode_literals
from django.shortcuts import render
from menu.models import Meal
# Create your views here.
def meals(request):
    meals = Meal.objects.all()
    return render(request, "meals.html", {"meals": meals})