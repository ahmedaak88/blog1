from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_detail(request, post_id):
    obj = get_object_or_404(Post , id = post_id)
    context = {
        "instance": obj,
    }
    return render(request, 'post_detail.html',context)

def post_list(request):
    details = Post.objects.all()#.order_by("-timestamp","-updated")
    paginator = Paginator(details, 4) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    context3 = {
        "user": request.user,
        "list": contacts,
    }
    return render(request, 'post_list.html',context3)

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request,"you are king of the world")
        return redirect ("post:list")
    context = {
    "form": form,
    }
    return render(request, 'post_create.html',context)

    
def post_update(request, post_id):
    post_obj = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None ,request.FILES or None,instance=post_obj)
    if form.is_valid():
        form.save()
        messages.success(request,"how dare you ?")
        return redirect ("post:list")
    context = {
    "form": form,
    "post_obj": post_obj,
    }
    return render(request, 'post_update.html',context)

def post_delete(request, post_id):
    post_obj = Post.objects.get(id=post_id)
    post_obj.delete()
    messages.warning(request, "dont you dare")
    return redirect("post:list")
    
