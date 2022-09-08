from django.db import models
import uuid
from datetime import datetime
from accounts.models import Profile
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to="post_images")
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(get_user_model(),related_name='image_post')
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user.user.first_name} {self.user.user.last_name}"

    def get_absolute_url(self):
        return reverse('images:post_detail', args=[str(self.id)])

