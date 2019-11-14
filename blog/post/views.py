from django.shortcuts import render
from post.models import Post
# Create your views here.


from markdown2 import Markdown
def post(request, id):
    markdowner = Markdown()
    posts = Post.objects.get(id=id)
    content = markdowner.convert(posts.content)
    return render(request, "post.html", {"post": posts, "content":content})

def showAll(request) :
    posts = Post.objects.all()
    return render(request, "post_all.html", {"posts": posts})