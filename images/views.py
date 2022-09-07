from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm
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
    
