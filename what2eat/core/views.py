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
        rl_org = List.objects.filter(user=request.user)
        rl = [x.restaurant for x in rl_org]
        rll = [x.restaurant.__dict__ for x in rl_org]
        for r, mod in zip(rl, rll) :
            c = Category.objects.filter(restaurant=r)
            c = [x.name for x in c]
            mod['categories'] = c
    except List.DoesNotExist:
        rl = []
    
    cl = [x.category.name for x in cl]
    return render(request, "splash.html", {"cl": cl, "rl": rll})

def accounts(request):
    return render(request, "accounts.html", {})

def search_view(request):
    if request.method == "POST":
        keyword = request.POST['searchKey']
        result = search(keyword)

        rl = List.objects.filter(user=request.user)
        rl = [x.restaurant.name for x in rl]

        for r in result:
            if r['name'] not in rl:
                r['seen'] = False
            else:
                r['seen'] = True

        return render(request, "search_result.html", {'keyword': keyword, 'result': result})
    return render(request, "search_result.html", {'keyword': keyword, 'result':[]}) 


def remove(request):
    r = Restaurant.objects.get(id=request.GET['id'])
    categories = Category.filter(restaurant=r)
    for c in categories:
        l  = List.objects.get(user=request.user, restaurant=r, category=c)
        if List.objects.filter(user=request.user, category=c).count == 1:
            cl = CategoryList.get(user=request.user, category=c)
            cl.delete()
        l.delete()
    return redirect('/')

def add(request):
    if request.method == "POST":
        idtmp = request.POST.get('rest_id')
        # categories = [x['alias'] for x in eval(request.POST['categories'])]
        categories = eval(request.POST.get('categories'))
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
            l.category = hashtag
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