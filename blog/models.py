from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone




class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

