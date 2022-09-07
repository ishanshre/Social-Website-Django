from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class IndexView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'images/index.html'

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'images/post_detail.html'
    