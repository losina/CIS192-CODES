from django.shortcuts import render, redirect 
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.models import Restaurant, Category, List, CategoryList
from core.yelp import search

def splash(request):
    try:
        cl = CategoryList.objects.filter(user=request.user)
    except CategoryList.DoesNotExist:
        cl = []
    try: 
        rl = List.objects.filter(user=request.user)
    except List.DoesNotExist:
        rl = []
    cl = [x.category.name for x in cl]
    return render(request, "splash.html", {"cl": cl, "rl": rl})

def accounts(request):
    return render(request, "accounts.html", {})

def search_view(request):
    if request.method == "POST":
        keyword = request.POST['searchKey']
        return render(request, "search_result.html", {'keyword': keyword, 'result': search(keyword)})
    return render(request, "search_result.html", {'keyword': keyword, 'result':[]}) 
def add(request):
    if request.method == "POST":
        idtmp = request.POST.get('rest_id')
        categories = [x['alias'] for x in eval(request.POST['categories'])]
 
        try:
            r =  Restaurant.objects.get(id=idtmp)
        except Restaurant.DoesNotExist:
            r = None  
        if not r:
            r = Restaurant.objects.create(id=idtmp, name=request.POST.get('name'), rating=request.POST.get('rating'), url=request.POST.get('url'), address=request.POST.get('address'))
            for c in categories:
                hashtag, created = Category.objects.get_or_create(name=c)
                hashtag.restaurant.add(r)
                hashtag.save()

        for h in categories: 
            hashtag = Category.objects.get(name=h)    
            try:
                cl = CategoryList.objects.get(category=hashtag, user=request.user)
            except CategoryList.DoesNotExist:
                cl = CategoryList()
                cl.user = request.user
                cl.category = hashtag
                cl.save()

        l = List()
        l.user = request.user
        l.restaurant = r
        l.save()
    return redirect('/')

def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, 'accounts.html', {})

def signup_view(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        login(request, user)
        return redirect('/')
    return render(request, 'accounts.html', {})

def logout_view(request):
    logout(request)
    return redirect("/login")