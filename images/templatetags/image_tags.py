from django import template
from ..models import Post

register=template.Library()
@register.simple_tag
def total_likes(pk):
    post = Post.objects.get(id=pk)
    return post.likes.all().count()