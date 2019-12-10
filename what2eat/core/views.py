from django.shortcuts import render, redirect 
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.models import Restaurant, Category, List, CategoryList
from core.yelp import search

#import necessary models for friendship module 
from friendship.models import Friend, Follow, Block
from friendship.models import FriendshipRequest

# fetch user data for the main page 
def splash(request):
    if request.user.is_authenticated:
        try:
            cl = CategoryList.objects.filter(user=request.user)
        except CategoryList.DoesNotExist:
            cl = []
        try: 
            rl_org = List.objects.filter(user=request.user)
            rl_org = list(set([x.restaurant for x in rl_org]))
            rll = [x.__dict__ for x in rl_org]
            for r, mod in  zip(rl_org, rll):
                c = Category.objects.filter(restaurant=r)
                c = [x.name for x in c]
                mod['categories'] = c
        except List.DoesNotExist:
            rll = []

        cl = [x.category.name for x in cl]
        return render(request, "splash.html", {"cl": cl, "rl": rll})
    else:
        return render(request, "splash.html")

# render accounts page for login/signup
def accounts(request):
    return render(request, "accounts.html", {})

# display search result of keyword in Yelp database
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


# remove saved restaurant from the list 
def remove(request):
    r = Restaurant.objects.get(id=request.GET['id'])
    l  = List.objects.filter(user=request.user, restaurant=r)
    # if the restaurant is the only associated restaurant with a category, remove that as well
    for ls in l:
        c = ls.category
        if List.objects.filter(user=request.user, category=c).count() == 1:
            cl = CategoryList.objects.get(user=request.user, category=c)
            cl.delete()
        ls.delete()

    return redirect('/')

# save a restaurant to the list
def add(request):
    if request.method == "POST":
        idtmp = request.POST.get('rest_id')
        # categories = [x['alias'] for x in eval(request.POST['categories'])]
        categories = eval(request.POST.get('categories'))
        try:
            r =  Restaurant.objects.get(id=idtmp)
        except Restaurant.DoesNotExist:
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

# django functionality for login 
def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, 'accounts.html', {})

# django functionality for signup 
def signup_view(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        login(request, user)
        return redirect('/')
    return render(request, 'accounts.html', {})

# django functionality for logout
def logout_view(request):
    logout(request)
    return redirect("/login")

#
#
#
# Friendship Functionalities 

#display friends page to manage friend requests 
def friends(request):
    friend_list = [f.username for f in Friend.objects.friends(request.user)]
    new_requests = Friend.objects.unread_requests(user=request.user)
    users = User.objects.all()
    users = sorted([u.get_username() for u in users if u != request.user and u.get_username() not in friend_list])

    return render(request, 'friends.html', {'friends': friend_list, 'requests':new_requests,'users':users})

#send friend request 
def friend_request(request):
    if request.method == "POST":
        friendname= request.POST['friendname']
        other_user = User.objects.get(username=friendname)
        try: 
            Friend.objects.add_friend(
            request.user,                              
            other_user,                                 
            message='Hi! I would like to add you to my friend list') 
        except:
            return redirect('/friends')
    return redirect('/friends')

# accept friend request
def accept_request(request):
    if request.method == "POST":
        req = request.POST.get('friendRequest')
        user = User.objects.get(username=req).id
        friend_request = FriendshipRequest.objects.filter(from_user=user)
        for f in friend_request:
            f.accept()
    return redirect('/friends')