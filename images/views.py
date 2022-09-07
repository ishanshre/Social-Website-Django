import profile
from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.

class IndexView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'images/index.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'images/post_detail.html'


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'images/post_create.html'
    message = 'Post Added'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message
    
    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        return super(PostCreateView, self).form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name  = 'images/post_update.html'
    message = "Post Updated"

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message
    
    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        return super(PostUpdateView, self).form_valid(form)
    
    def test_func(self):
        self.object = self.get_object()
        return self.object.user == self.request.user.profile


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'images/post_delete.html'
    message = 'Post Deleted'
    success_url = reverse_lazy('images:index')
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message
    
    def test_func(self):
        self.object = self.get_object()
        return self.object.user == self.request.user.profile