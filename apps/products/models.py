# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ProductManager(models.Manager):
    def validate_product(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "The title needs to be 2 or more characters."
        if len(postData['short_desc']) < 5:
            errors['short_desc'] = "The short description needs to be 5 or more characters."
        if len(postData['desc']) < 10:
            errors['desc'] = "Your description needs to be 10 or more characters."
        return errors
class Product(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=300)
    desc = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()


class Category(models.Model):
    name = models.CharField(max_length=40)
    products = models.ForeignKey(Product, related_name="category")