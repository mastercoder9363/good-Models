from django.db import models

class Post(models.Model):
    name=models.CharField(max_length=31)
    old=models.IntegerField(default=16)
    about=models.TextField()
