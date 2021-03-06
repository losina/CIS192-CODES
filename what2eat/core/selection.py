from django.shortcuts import render, redirect 
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.models import Restaurant, Category, List, CategoryList
from core.yelp import recommend

from friendship.models import Friend, Follow, Block
from friendship.models import FriendshipRequest

# show all list of friends in the first step of selection mode 
def selection_user(request):
    users = friend_list = [f.username for f in Friend.objects.friends(request.user)]
    return render(request, 'selection_user.html', {'users': users})

# show all categories saved by different users in the second step of selection mode  
def selection_cat(request):
    users = request.POST.getlist('user')
    users.append(request.user.username)
    categories = []
    for u in users:
        u = User.objects.get(username=u)
        print(u)
        cl = List.objects.filter(user=u)
        print(cl)
        for c in cl:
            if c.category.name not in categories:
                categories.append(c.category.name)

    return render(request, 'selection_category.html', {'categories': sorted(categories), 'users':users })

# show the top 5 result of recommendation 
def selection_result(request):
    categories = request.POST.getlist('category')
    print('categories', categories)
    users = eval(request.POST.get('users'))
    result = []
    redun = []
    for u in users:
        u = User.objects.get(username=u)
        rl = List.objects.filter(user=u)
        for r in rl:
            r = r.restaurant
            if r not in result:
                c = Category.objects.filter(restaurant=r)
                for cc in c:
                    if cc.name in categories:
                        result.append(r)
                        redun.append(r.name)
                        break
    result = sorted(result, key=lambda x: x.rating, reverse=True)
    recommendation = recommend(categories, redun)
    if len(result) > 5:
        result = result[:5]
    return render(request, 'selection_result.html', {"result": result, "recomm": recommendation})