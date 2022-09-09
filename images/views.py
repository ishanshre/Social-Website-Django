import profile
from urllib import request
from xml.etree.ElementTree import Comment
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm, CommentForm
from accounts.forms import Profile
from django.urls import reverse_lazy, reverse
# Create your views here.

class IndexView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'images/index.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        user_profile = Profile.objects.get(user = self.request.user.id)
        suggest = Profile.objects.all().exclude(following__in=[user_profile.user])
        context['suggest'] = suggest
        return context

class CommentGet(DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'images/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        postLikes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = postLikes.total_likes()
        liked = False
        if postLikes.likes.filter(id=self.request.user.profile.id).exists():
            liked=True
        context['form']=CommentForm()
        context['total_likes'] = total_likes
        context['liked']=liked
        return context

class CommentPost(LoginRequiredMixin, SingleObjectMixin,FormView):
    model = Post
    context_object_name = 'posts'
    template_name = 'images/post_detail.html'
    form_class = CommentForm
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form, *args, **kwargs):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user.profile
        comment.save()
        return super().form_valid(request, *args, **kwargs)

    def get_success_url(self):
        post_comment = self.get_object()
        return reverse('images:post_detail', args=[str(post_comment.id)])


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    def post(self, request,*args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)



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

