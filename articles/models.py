from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# An article has foreign key user.

class Article(models.Model):
    user = models.ForeignKey(User,blank=True,default=1)
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.title
        
        
# A comment has foreign key association with a user as well as article
class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments')
    user = models.ForeignKey(User, blank=True, default=1)
    text = models.TextField()
    date = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.text
