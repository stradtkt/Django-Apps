# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import *

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, 'users/index.html', context)

def edit(request, id):
    return render(request, 'users/user-edit.html')
    
def delete(request, id):
    person = User.objects.get(id=id).delete()
    return redirect('/users')

def profile(request, id):
    user = User.objects.get(id=id)
    context = {"user": user}
    return render(request, 'users/profile.html', context)