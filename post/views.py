from __future__ import unicode_literals
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm

def post_detail(request, post_id):
    obj = get_object_or_404(Post , id = post_id)
    context = {
        "instance": obj,
    }
    return render(request, 'post_detail.html',context)

#def post_detail(request):
#   details = Post.objects.filter(title__contains="something")
#    context2 = {
#        "user": request.user,
#        "list": details,
#    }
#    return render(request, 'post_detail.html',context2)

def post_list(request):
    details = Post.objects.all()
    context3 = {
        "user": request.user,
        "list": details,
    }
    return render(request, 'post_list.html',context3)
def post_create(request):
    form = PostForm()
    context = {
    "form": form,
    }
    return render(request, 'post_create.html',context)

    
def post_update(request):
    return render(request, 'post_update.html',{})

def post_delete(request):
    return render(request, 'post_delete.html',{})
