from django import template
from ..models import Post
from accounts.models import Profile
from django.shortcuts import get_object_or_404
register=template.Library()
@register.simple_tag
def total_likes(pk):
    post = Post.objects.get(id=pk)
    return post.likes.all().count()


@register.simple_tag
def total_following(pk):
    user_profile = Profile.objects.get(user = pk)
    following = Profile.objects.filter(following__in=[user_profile.user])
    return following.count()

