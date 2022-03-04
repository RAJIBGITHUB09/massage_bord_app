from django.contrib import admin

from .models import Post # importing the post from .models

# Register your models here.

admin.site.register(Post) # registaring the post 