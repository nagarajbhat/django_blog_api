from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Article(models.Model):
    user = models.ForeignKey(User,blank=True,default=1)
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.title
        
        
