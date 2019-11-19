from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.models import Tweet
import re
# Create your views here.
def splash(request):
    # create post
    if request.method == "POST":
        body = request.POST["body"]
        hashtag = re.findall(r"#(\w+)", body)
        Note.objects.create(title=title, body=body, author=request.user, hashtag = hashtag)
        return redirect("/")
    else:
        if request.user.is_authenticated:
            notes = Note.objects.filter(author=request.user)
        else:
            notes = []
        return render(request, "splash.html", {"notes": notes})

def accounts(request):
    return render(request, "accounts.html", {})

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