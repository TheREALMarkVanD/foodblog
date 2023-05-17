
from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from .models import recipe, recipe_card,Comment
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    posts=recipe.objects.all()
    return render(request,'app/TheIndianCulinarist.html',{"posts":posts})
def display(request,topic):
    if request.method == "POST":
        comment=request.POST.get('comment')
        if len(comment)<1:
            messages.error(request, "comment must not be empty")        
            return HttpResponseRedirect(request.path_info)
        user=request.user
        post=recipe.objects.get(title=topic)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=Comment(comments= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= Comment.objects.get(sno=parentSno)
            comment=Comment(comments= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")

    article=recipe.objects.get(title=topic)
    card=recipe_card.objects.get(myfk=article)
    comments= Comment.objects.filter(post=article,parent=None)

    replies= Comment.objects.filter(post=article).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    return render(request,'app/display.html',{"article":article,"card":card,'comments': comments, 'user': request.user,'replyDict': replyDict})

def search(request):
    search=request.GET['search']
    if len(search)>78:
        results=Post.objects.none()
    else:
        resultstitle=recipe.objects.filter(title__icontains=search)
        resultsdesc=recipe.objects.filter(desc__icontains=search)
        results=resultstitle.union(resultsdesc)
    if results.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")

    return render(request,'app/search.html',{"results":results,"search":search})
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        if len(username)>12:
            messages.error(request, "Username must be under 12 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username should only contain only letters and numbers")
            return redirect('home')
        if pass1!=pass2:
            messages.error(request, "passwords do not match.")
            return redirect('home')

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"account created")
        return redirect('home')

def handlelogin(request):
    username1=request.POST['loginusername']
    password1=request.POST['loginpassword']#should be same in html page id and name
    user=authenticate(username=username1 ,password=password1)
    if user is not None:
        login(request, user)
        messages.success(request,"successfully logged in")
        return redirect('home')
    else: 
        messages.error(request,"Invalid credentials, please try again.")
        return redirect('home')
def handlelogout(request):
    logout(request)
    messages.success(request, "successfully logged out!")
    return redirect('home')
def index(request,category):
    if category=='southindian':
        category='South Indian'
        posts=recipe.objects.filter(region='South Indian')
    elif category=='northindian':
        category='North Indian'
        posts=recipe.objects.filter(region='North Indian')
    elif category=='indochinese':
        category='Indo-Chinese'
        posts=recipe.objects.filter(region='Indo-Chinese')
    return render(request,'app/index.html',{"category":category,"posts":posts})
