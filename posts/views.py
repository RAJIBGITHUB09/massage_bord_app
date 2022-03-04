from re import template
from django.shortcuts import render

#importing listview from django.views.generic 
from django.views.generic import ListView

#importing post from .models
from .models import Post



# Create your views here.

class HomePageView(ListView):
    model=Post
    template_name ='home.html'
    context_object_name= 'all_posts_list' 