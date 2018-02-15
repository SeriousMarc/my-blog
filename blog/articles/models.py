from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True) # let user set data
    #description
    #slug
    #section
    #author

    def __str__(self):
        return self.title
