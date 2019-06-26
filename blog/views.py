from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    # DetailView send the context object which is used to show data
    # usign template. DetailView will send either our "model_name(in lowercase)"
    # or "object". we can change it by using "context_object_name = 'name of object'".
