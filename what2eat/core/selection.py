from django.shortcuts import render, redirect 
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.models import Restaurant, Category, List, CategoryList

def selection_user(request):
    users = User.objects.all()
    users = sorted([u.get_username() for u in users if u != request.user])
    return render(request, 'selection_user.html', {'users': users})

def selection_cat(request):
    categories = sorted([c.name for c in Category.objects.all()])

    return render(request, 'selection_category.html', {'categories': categories, 'users':request.POST.getlist('user') })

def selection_result(request):
    categories = request.POST.getlist('category')
    print('categories', categories)
    users = eval(request.POST.get('users'))
    result = []
    for u in users:
        u = User.objects.get(username=u)

        rl = List.objects.filter(user=u)
        print('rl', rl)
        for r in rl:
            r = r.restaurant
            c = Category.objects.filter(restaurant=r)
            for cc in c:
                if cc.name in categories:
                    result.append(r)
                    break
    print(result)
    return render(request, 'selection_result.html')