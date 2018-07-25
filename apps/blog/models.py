# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..users.models import User
# Create your models here.

class PostManager(models.Manager):
    def validate_post(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "The title needs to be 2 or more characters."
        if len(postData['body']) < 10:
            errors['body'] = "The body of the post needs to be 10 or more characters."
        return errors

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    users = models.ForeignKey(User, related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

class CommentManager(models.Manager):
    def validate_comment(self, postData):
        if len(postData['body']) < 3:
            errors['body'] = "Your comment needs to be 3 or more characters."


class Comment(models.Model):
    users = models.ForeignKey(User, related_name="commentor")
    posts = models.ForeignKey(Post, related_name="post")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()