from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.models import Tweet, HashTag, Like

import requests
import json
import re

#set up yelp api 
api_key='-4s2dP9Rl9T0e30DOmljIoReMpCfCx4UWxAGPJBkXFEuJy-dzf-iwClrVnPk0s1Mb63a9pFAC75GC6xrX4dvlT0GL6_SIrbt90dwA-X38IodBSxUj79ZtdNpfN3uXXYx'
headers = {'Authorization': 'Bearer %s' % api_key}
 
# Create your views here.
def splash(request):
    # create post
    if request.method == "POST":
        body = request.POST["body"]
        hashtags = set(re.findall(r"#(\w+)", body))
        tw = Tweet.objects.create(body=body, author=request.user)
        for word in hashtags:
            hashtag, created = HashTag.objects.get_or_create(name=word)
            hashtag.tweet.add(tw)
        return redirect("/")
    else:
        if request.user.is_authenticated:
            tweets = Tweet.objects.all().order_by('-created_at')
            t_list = []
            for t in tweets:
                like = Like.objects.filter(user=request.user, tweet=t)
                like = True if like else False 
                t_list.append({"id": t.id, "author": t.author, "time": t.created_at,"body": t.body, "like":like, "like_num": t.likes})
            h_list = HashTag.objects.all()
        else:
            t_list = []
            h_list = []
        return render(request, "splash.html", {"tweets": t_list, "hashtags":h_list})

def accounts(request):
    return render(request, "accounts.html", {})
def profile(request):
    user = User.objects.get(username=request.GET['user'])
    tweets = Tweet.objects.filter(author=user).order_by('-created_at')
    t_list = []
    for t in tweets:
        like = Like.objects.filter(user=request.user, tweet=t)
        like = True if like else False 
        t_list.append({"id": t.id, "author": t.author, "body": t.body, "time": t.created_at, "like":like, "like_num": t.likes})
    return render(request, "profile.html", {"author": user, "tweets": t_list})

def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("/")
        print(user)
    return render(request, 'accounts.html', {})

def hashtag(request):
    h = HashTag.objects.get(name=request.GET['name'])
    tweets = h.tweet.all()

    return render(request, "hashtag.html", {"hashtag": h, "tweets": tweets})

def signup_view(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        login(request, user)
        return redirect('/')
    return render(request, 'accounts.html', {})

def logout_view(request):
    logout(request)
    return redirect("/login")

def like(request):
    tw = Tweet.objects.get(id=request.GET['id'])
    new_like = Like()
    new_like.tweet = tw
    new_like.user = request.user
    new_like.save()
    tw.likes += 1
    tw.save()

    return redirect('/')
def delete(request):
    tw = Tweet.objects.get(id=request.GET['id'])
    for h in HashTag.objects.filter(tweet=tw):
        if len(h.tweet.all()) == 1:
            h.delete()
    tw.delete()
    return redirect('/')

def unlike(request):
    tw = Tweet.objects.get(id=request.GET['id'])

    like = Like.objects.get(tweet=tw, user=request.user)
    print(like)
    like.delete()
    tw.likes -= 1
    tw.save()
    return redirect('/')