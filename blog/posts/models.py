from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    creation_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    user = models.ForeignKey(User)