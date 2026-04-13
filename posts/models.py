from django.db import models

class Post(models.Model): # new
    text = models.TextField()

# Create your models here.
    def __str__(self): # new
        return self.text[:50]