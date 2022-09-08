import profile
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
# Create your views here.

class IndexView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'images/index.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'images/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args,**kwargs)
        postLikes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = postLikes.total_likes()
        liked = False
        if postLikes.likes.filter(id=self.request.user.profile.id).exists():
            liked=True
        context['total_likes'] = total_likes
        context['liked']=liked
        return context


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

#logic for like/unline function
def LikeView(request, pk):
    post = get_object_or_404(Post, id=str(request.POST.get('post_id')))
    if post.likes.filter(id=request.user.profile.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('images:post_detail', args=[str(pk)]))

