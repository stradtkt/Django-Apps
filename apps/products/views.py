# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products/index.html', context)

def add_product_page(request):
    add_prod = AddProductForm()
    context = {
        "add_prod": add_prod
    }
    return render(request, 'products/add-product.html', context)

def process_product(request):
    errors = Product.objects.validate_product(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/products/add_product')
    else:
        title = request.POST['title']
        short_desc = request.POST['short_desc']
        desc = request.POST['desc']
        price = request.POST['price']
        image = request.POST['image']
        Product.objects.create(title=title, short_desc=short_desc, desc=desc, price=price, image=image)
        messages.success(request, 'Product Successfully Added')
        return redirect('/products')