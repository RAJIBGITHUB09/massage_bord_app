from django.db import models

# Create your models here.

# down code writen by rajib 

class Post(models.Model):
    text=models.TextField()

    def __str__(self):        # adding this __str__ function 
        return self.text[:50]