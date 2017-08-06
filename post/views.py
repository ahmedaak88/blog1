from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from .forms import PostForm , UserSignUp ,UserLogin 
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, JsonResponse
from django.utils import timezone 
from django.db.models import Q
from django.contrib.auth import authenticate , login ,logout

def search_bar(request):
    obj = Post.objects.all()
    details = []
    for x in obj:
        details = details + [x.title]
    context = {
    "details": details,
    }
    return JsonResponse(context,safe=False)


def like_botton(request, post_id):
    obj = Post.objects.get(id=post_id)
    like , created =Like.objects.get_or_create(user=request.user, post=obj)
    
    if created:
        action="like"
    else:
        action="unlike"
        like.delete()

    post_like_count = obj.like_set.all().count()
    context = {
        "like_count": post_like_count,
        "action":action ,

    }

    return JsonResponse(context, safe=False)

def userlogin(request):
    context={}
    form = UserLogin()
    context['form'] = form 
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user= authenticate(username=username,password=password)
            if auth_user is not None:
                login(request,auth_user)
                return redirect("post:home")

            messages.warning(request,"wrong user name or password")
            return redirect("post:login")
        messages.warning(request,form.errors)
        return redirect("post:login")
    return render(request, 'login.html',context)


def usersignup(request):
    context={}
    form = UserSignUp()
    context['form'] = form 
    if request.method == "POST":
        form = UserSignUp(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = user.password
            user.set_password(password)
            user.save()
            auth_user= authenticate(username=username,password=password)
            login(request,auth_user)
            return redirect("post:home")
        messages.error(request,form.errors)
        return redirect("post:signup")
    return render(request, 'signup.html',context)

def userlogout(request):
    logout(request)
    return redirect("post:home")

def post_home(request):
    obj = Post.objects.all().first()
    context = {
    "user": request.user,
    "post_last": obj,
    }
    return render(request, 'post_home.html', context)
def post_detail(request, slug):
    obj = get_object_or_404(Post , slug=slug)
    # date = timezone.now().date()
    # if obj.publish > date or obj.draft:
    #     if not(request.user.is_staff or request.user.is_superuser):
    #         raise   Http404
    # if request.user.is_authenticated():
    #     if Like.objects.filter(post=obj, user=request.user).exists():
    #         liked= True 
    #     else:
    #         liked = False
    # post_like_count = obj.like_set.all().count()
    
    context = {
        "user":request.user,
        "instance": obj,
        # "liked": liked,
        # "like_count" : post_like_count,
    }
    return render(request, 'post_detail.html',context)

def post_list(request):
    today = timezone.now().date()
    if request.user.is_staff or request.user.is_superuser:
        details= Post.objects.all()
    else:
        details = Post.objects.filter(draft=False).filter(publish__lte=today)

    query = request.GET.get("q")
    if query:
        details= details.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) | 
            Q(author__last_name__icontains=query)
            ).distinct()
    paginator = Paginator(details, 4) # Show 4 contacts per page

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
        "today": today,
    }
    return render(request, 'post_list.html',context3)

def post_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit= False)
        obj.author = request.user 
        obj.save()
        messages.success(request,"you are king of the world")
        return redirect ("post:list")
    context = {
    "form": form,
    "user": request.user
    }
    return render(request, 'post_create.html',context)

    
def post_update(request, slug):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    post_obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None ,request.FILES or None,instance=post_obj)
    if form.is_valid():
        form.save()
        messages.success(request,"how dare you ?")
        return redirect ("post:list")
    context = {
    "user":request.user,
    "form": form,
    "post_obj": post_obj,
    }
    return render(request, 'post_update.html',context)

def post_delete(request, slug):
    if not (request.user.is_superuser):
        raise Http404
    post_obj = Post.objects.get(slug=slug)
    post_obj.delete()
    messages.warning(request, "dont you dare")
    return redirect("post:list")
    
