# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ..users.models import *

# Create your views here.
def index(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'main/index.html', context)