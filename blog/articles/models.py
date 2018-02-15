from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True) # let user set data
    slug = models.SlugField(blank=True)
    #section = if User = administration or users
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
