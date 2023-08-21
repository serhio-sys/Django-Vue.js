from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    created = models.DateTimeField("Created",auto_now=True)
    name = models.CharField("Name of post", max_length=40)
    desc = models.TextField()
    likes = models.PositiveIntegerField(blank=True,default=0)
    liked = models.ManyToManyField(get_user_model(),related_name="liked",blank=True)
    author = models.ForeignKey(get_user_model(),verbose_name="Author",on_delete=models.CASCADE)