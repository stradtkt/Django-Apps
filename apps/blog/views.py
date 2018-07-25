# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here.
def index(request):
    blog = Post.objects.all()
    context = {
        "blog": blog
    }
    return render(request, 'blog/index.html', context)

def add_blog(request):
    add_blog = AddBlogForm()
    context = {
        "add_blog": add_blog
    }
    return render(request, 'blog/add-blog.html', context)

def post(request, id):
    blog = Post.objects.get(id=id)
    com_form = AddCommentForm()
    context = {
        "blog": blog,
        "comment": com_form,
    }
    return render(request, 'blog/single-post.html', context)

def delete_post(request, id):
    post = Post.objects.get(id=id).delete()
    messages.success(request, "Post Successfully Deleted")
    return redirect('/blog')

def process_blog(request):
    errors = Post.objects.validate_post(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')
    else:
        title = request.POST['title']
        body = request.POST['body']
        users = User.objects.get(id=request.session['id'])
        Post.objects.create(title=title, body=body, users=users)
        messages.success(request, "Blog posted successfully")
        return redirect('/blog')

def process_comment(request, id):
    errors = Comment.objects.validate_comment(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/{}/post'.format(id))
    else:
        body = request.POST['body']
        users = User.objects.get(id=request.session['id'])
        posts = Post.objects.get(id=id)
        Comment.objects.create(body=body, users=users, posts=posts)
        messages.success(request, "Added Comment")
        return redirect('/{}/post'.format(id))
